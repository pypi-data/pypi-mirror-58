# Copyright 2016 Red Hat, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import logging
import traceback
import uuid
import webob.exc

from oslo_config import cfg

from novajoin import base
from novajoin import exception
from novajoin.glance import get_default_image_service
from novajoin.ipa import IPAClient
from novajoin import keystone_client
from novajoin import policy
from novajoin import util


CONF = cfg.CONF

LOG = logging.getLogger(__name__)


def create_join_resource():
    return base.Resource(JoinController())


def response(code):
    """Attaches response code to a method.

    This decorator associates a response code with a method.  Note
    that the function attributes are directly manipulated; the method
    is not wrapped.
    """

    def decorator(func):
        func.wsgi_code = code
        return func
    return decorator


class Join(base.APIRouter):
    """Route join requests."""

    def _setup_routes(self, mapper, ext_mgr):
        self.resources['join'] = create_join_resource()
        mapper.connect('join', '/',
                       controller=self.resources['join'],
                       action='create')
        mapper.redirect('', '/')


class Controller(object):
    """Default controller."""

    _view_builder_class = None

    def __init__(self, view_builder=None):
        """Initialize controller with a view builder instance."""
        if view_builder:
            self._view_builder = view_builder
        else:
            self._view_builder = None


class JoinController(Controller):

    def __init__(self, ipaclient=IPAClient()):
        super(JoinController, self).__init__(None)
        self.ipaclient = ipaclient

    def _get_allowed_hostclass(self, project_name):
        """Get the allowed list of hostclass from configuration."""
        try:
            group = CONF[project_name]
        except cfg.NoSuchOptError:
            # dynamically add the group into the configuration
            group = cfg.OptGroup(project_name, 'project options')
            CONF.register_group(group)
            CONF.register_opt(cfg.ListOpt('allowed_classes'),
                              group=project_name)
        try:
            allowed_classes = CONF[project_name].allowed_classes
        except cfg.NoSuchOptError:
            LOG.error('No allowed_classes config option in [%s]', project_name)
            return []
        else:
            if allowed_classes:
                return allowed_classes
            else:
                return []

    @response(200)
    def create(self, req, body=None):
        """Generate the OTP, register it with IPA

        Options passed in but as yet-unused are and user-data.
        """

        # Set message id to zero for now.
        # We could set it to the request_id in the python-request,
        # but this is already logged as part of the server logs.
        message_id = 0

        if not body:
            LOG.error('No body in create request')
            raise base.Fault(webob.exc.HTTPBadRequest())

        context = req.environ.get('novajoin.context')
        try:
            policy.authorize_action(context, 'join:create')
        except exception.PolicyNotAuthorized:
            raise base.Fault(webob.exc.HTTPForbidden())

        hostname_short = body.get('hostname')
        if not hostname_short:
            LOG.error('No hostname in request')
            raise base.Fault(webob.exc.HTTPBadRequest())

        metadata = body.get('metadata', {})
        enroll = metadata.get('ipa_enroll', '').lower() == 'true'

        image_metadata = {}
        if not enroll:
            LOG.debug('IPA enrollment not requested in instance creation')
            # Check the image metadata to see if enrollment was requested

            image_id = body.get('image-id')
            if not image_id:
                LOG.error('No image-id in request')
                raise base.Fault(webob.exc.HTTPBadRequest())
            image_service = get_default_image_service()
            try:
                image = image_service.show(context, image_id)
            except (exception.ImageNotFound,
                    exception.ImageNotAuthorized) as e:
                msg = 'Failed to get image: %s' % e
                LOG.error(msg)
                raise base.Fault(webob.exc.HTTPBadRequest(explanation=msg))
            else:
                image_metadata = image.get('properties', {})

            enroll = image_metadata.get('ipa_enroll', '').lower() == 'true'
            if not enroll:
                LOG.debug('IPA enrollment not requested in image')
                return {}
            else:
                LOG.debug('IPA enrollment requested in image')
        else:
            LOG.debug('IPA enrollment requested as property')

        hostclass = metadata.get('ipa_hostclass')
        if hostclass:
            # Only look up project_name when hostclass is requested to
            # save a round-trip with Keystone.
            project_id = body.get('project-id')
            if not project_id:
                LOG.error('No project-id in request')
                raise base.Fault(webob.exc.HTTPBadRequest())

            project_name = keystone_client.get_project_name(project_id)
            if project_name is None:
                msg = 'No such project-id, %s' % project_id
                LOG.error(msg)
                raise base.Fault(webob.exc.HTTPBadRequest(explanation=msg))

            allowed_hostclass = self._get_allowed_hostclass(project_name)
            LOG.debug('hostclass %s, allowed_classes %s' %
                      (hostclass, allowed_hostclass))
            if (hostclass not in allowed_hostclass and
                    '*' not in allowed_hostclass):
                msg = "Not allowed to add to hostclass '%s'" % hostclass
                LOG.error(msg)
                raise base.Fault(webob.exc.HTTPForbidden(explanation=msg))
        else:
            project_name = None

        data = {}

        ipaotp = uuid.uuid4().hex
        instance_id = body.get('instance-id', '')

        data['hostname'] = util.get_fqdn(hostname_short, project_name)
        _, realm = self.ipaclient.get_host_and_realm()
        data['krb_realm'] = realm

        try:
            data['ipaotp'] = self.ipaclient.add_host(data['hostname'], ipaotp,
                                                     metadata, image_metadata,
                                                     instance_id, message_id)
            if not data['ipaotp']:
                # OTP was not added to host, don't return one
                del data['ipaotp']
        except exception.DuplicateInstanceError as ee:
            # NOTE(hrybacki): This likely means an attempt to add a host with
            #                 a hostname that has already enrolled. Look for
            #                 a Forbidden (HTTP 403) in nova-compute.logs
            raise base.Fault(webob.exc.HTTPForbidden(explanation=ee.msg))
        except Exception as e:  # pylint: disable=broad-except
            LOG.error('adding host failed %s', e)
            LOG.error(traceback.format_exc())

        self.ipaclient.start_batch_operation(message_id)
        # key-per-service
        managed_services = [metadata[key] for key in metadata.keys()
                            if key.startswith('managed_service_')]
        if managed_services:
            self.add_managed_services(
                data['hostname'], managed_services, message_id)

        compact_services = util.get_compact_services(metadata)
        if compact_services:
            self.add_compact_services(
                hostname_short, compact_services, message_id)

        self.ipaclient.flush_batch_operation(message_id)

        return data

    def add_managed_services(self, base_host, services, message_id=0):
        """Make any host/principal assignments passed into metadata."""
        LOG.debug("[%s] In add_managed_services", message_id)

        hosts_found = list()
        services_found = list()

        for principal in services:
            principal_host = principal.split('/', 1)[1]

            # add host if not present
            if principal_host not in hosts_found:
                self.ipaclient.add_subhost(principal_host, message_id)
                hosts_found.append(principal_host)

            # add service if not present
            if principal not in services_found:
                self.ipaclient.add_service(principal, message_id)
                services_found.append(principal)

            self.ipaclient.service_add_host(principal, base_host, message_id)

    def add_compact_services(self, base_host_short, service_repr,
                             message_id=0):
        """Make any host/principal assignments passed from metadata

        This takes a dictionary representation of the services and networks
        where the services are listening on, and forms appropriate
        hostnames/service principals based on this information.
        The dictionary representation looks as the following:

            {
                "service1": [
                    "network1",
                    "network2"
                ],
                "service2": [
                    "network2",
                    "network3"
                ],
            }

        This function will then use the short hostname given for the node, and
        will form the service principals. So, for the example above, the
        resulting principals would be:

            service1/hostname-short.network1.novajoindomain
            service1/hostname-short.network2.novajoindomain
            service2/hostname-short.network2.novajoindomain
            service3/hostname-short.network2.novajoindomain

        assuming that the hostname given in the body of the request was
        "hostname-short" and that the domain is called "novajoindomain".

        This attempts to do a more compact representation since the nova
        metadta entries have a limit of 255 characters.
        """
        LOG.debug("[%s] In add_compact_services", message_id)

        hosts_found = list()
        services_found = list()
        base_host = util.get_fqdn(base_host_short)

        for service_name, net_list in service_repr.items():
            for network in net_list:
                host_short = "%s.%s" % (base_host_short, network)
                principal_host = util.get_fqdn(host_short)
                principal = "%s/%s" % (service_name, principal_host)

                # add host if not present
                if principal_host not in hosts_found:
                    self.ipaclient.add_subhost(principal_host, message_id)
                    hosts_found.append(principal_host)

                # add service if not present
                if principal not in services_found:
                    self.ipaclient.add_service(principal, message_id)
                    services_found.append(principal)

                self.ipaclient.service_add_host(
                    principal, base_host, message_id)
