# Copyright 2019 Antidot opensource@antidot.net
#
# This file is part of Fluid-Topics python API
#
# Fluid-Topics python API is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation; either version 2 of
# the License, or (at your option) any later version.
#
# Fluid-Topics python API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import base64
from typing import List

from deprecated.sphinx import deprecated
from pynject import Injector, Module

from fluidtopics.connector.internal.constants import PUBLISH_FILE, ACTION_FILE
from fluidtopics.connector.internal.fson.fson_publication import PublicationConverter
from fluidtopics.connector.internal.sender import RemoteSender
from fluidtopics.connector.internal.zip_builder import FsonZipBuilder
from fluidtopics.connector.model.attachment_update import AttachmentsUpdate
from fluidtopics.connector.model.metadata_update import MetadataUpdates
from fluidtopics.connector.model.publication import Publication
from fluidtopics.connector.model.right_update import RightsUpdates


class Client:
    """
    Entry point for adding, deleting and updating publications.
    """

    def publish(self, *publications: Publication):
        """ Create or update a publication
        """
        raise NotImplementedError()

    @deprecated(reason='Prefer using content access right rules than setting rights by publication.')
    def update_rights(self, rights_updates: RightsUpdates):
        """ Update rights of given publications
        """
        raise NotImplementedError()

    def update_metadata(self, meta_updates: MetadataUpdates):
        """ Update or Replace metadata of given publications
        """
        raise NotImplementedError()

    def update_attachments(self, attachments_updates: AttachmentsUpdate):
        """ Update attachments and links between publications and attachments
        """
        raise NotImplementedError()

    def delete(self, publication_ids: List[str]):
        """ Delete the specified publications
        """
        raise NotImplementedError()

    def delete_all(self):
        """ Delete all publications from this source
        """
        raise NotImplementedError()


class Authentication:
    """Authentication interface for the RemoteClient."""

    def basic_authentication(self) -> str:
        raise NotImplementedError(
            "Please provide an object with an attribute 'basic_authentication' that return 'login:password'"
            'encoded as base 64. See : https:/'
            '/www.ibm.com/support/knowledgecenter/en/SSGMCP_5.1.0/com.ibm.cics.ts.internet.doc/topics/dfhtl2a.html'
        )


class LoginAuthentication(Authentication):
    """Authentication using login/password for the RemoteClient."""

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def basic_authentication(self) -> str:
        bytes_encoded = bytes('{}:{}'.format(self.login, self.password), 'utf-8')
        b64_encoded = base64.b64encode(bytes_encoded)
        return b64_encoded.decode('utf-8')


class Base64Authentication(Authentication):
    """Authentication method which set directly the value of the Authorization http header."""

    def __init__(self, basic_authentication: str):
        self._authentication = basic_authentication

    def basic_authentication(self) -> str:
        return self._authentication


class RemoteClient(Client):
    """Implementation of the Client interface which use Fluid Topics webservices."""

    def __init__(self, url: str, authentication: Authentication, source_id: str):
        """Create a RemoteClient.

        :param url: URL of the Fluid Topics server (like "http://doc.antidot.net")
        :param authentication: user (with KHUB_ADMIN rights) used to call webservices
        :param source_id: ID of the source in Fluid Topics used for this connector"""
        self._sender = RemoteSender(url, authentication.basic_authentication(), source_id)
        injector = Injector(Module())
        self._fluid_converter = injector.get_instance(PublicationConverter)

    def __repr__(self):
        return 'RemoteClient:[url={}, source_id={}]'.format(self._sender.url, self._sender.source_id)

    def publish(self, *publications: Publication):
        fson_zip = FsonZipBuilder()
        fson_zip.add_data(PUBLISH_FILE, '{"dataMode": "INCREMENTAL", "version": "1.0"}')  # TODO: remove after POC
        fson_zip.add_data(ACTION_FILE, '{"type": "publish"}')  # TODO: remove after POC
        for publication in publications:
            fson_publication = self._fluid_converter.convert_publication(publication)
            fson_zip.add_publication(fson_publication)
            for resource in publication.resources:
                fson_file = self._fluid_converter.convert_resource(resource)
                fson_zip.add_resource(fson_file, resource.content)
        return self._sender.send(fson_zip.build(), 'publish.zip')

    def update_rights(self, rights_updates: RightsUpdates):
        raise NotImplementedError()

    def update_metadata(self, meta_updates: MetadataUpdates):
        raise NotImplementedError()

    def update_attachments(self, attachments_updates: AttachmentsUpdate):
        raise NotImplementedError()

    def delete(self, publication_ids: List[str]):
        raise NotImplementedError()

    def delete_all(self):
        raise NotImplementedError()
