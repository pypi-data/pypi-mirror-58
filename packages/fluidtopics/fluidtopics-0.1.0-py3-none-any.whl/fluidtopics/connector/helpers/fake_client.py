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

from typing import List, Optional

from assertpy import assert_that, fail
from deprecated.sphinx import deprecated
from pynject import singleton

from fluidtopics.connector.client import Client
from fluidtopics.connector.helpers.attachment_update_checker import AttachmentChecker, AttachCommandChecker, \
    DetachCommandChecker
from fluidtopics.connector.helpers.metadata_update_checker import PublicationMetadataChecker
from fluidtopics.connector.helpers.publication_checker import PublicationChecker, RightsChecker
from fluidtopics.connector.model.attachment_update import AttachmentsUpdate
from fluidtopics.connector.model.metadata_update import MetadataUpdates
from fluidtopics.connector.model.publication import Publication
from fluidtopics.connector.model.right_update import RightsUpdates


@singleton
class FakeClient(Client):
    """FakeClient is a helper to mock a Client."""

    def __init__(self):
        self._publications = []
        self._rights_update = {}
        self._meta_update = {}
        self._deletions = []
        self._delete_all = False
        self._attachments_update = None

    def publish(self, *publications: Publication):
        self._publications.extend(publications)

    def publications(self) -> List[PublicationChecker]:
        """Return checkers on all published Publications."""
        return [PublicationChecker(pub) for pub in self._publications]

    def publication(self, pub_id: str) -> PublicationChecker:
        """Return a checker on a Publication.

        :param pub_id: ID of the Publication to check.
        :return A PublicationChecker to make asserts on the Publication.
        :raises:
            AssertionError: No Publication was published with this ID."""
        publication = self._publication_checker(pub_id)
        assert_that(publication).described_as('{} not found in published publications: {}'
                                              .format(pub_id, [pub.id for pub in self._publications])) \
            .is_not_none()
        return publication

    def assert_not_published(self, pub_id: str):
        """Assert that no publication have been published with this ID."""
        publication = self._publication_checker(pub_id)
        assert_that(publication).described_as('{} is published'.format(pub_id)) \
            .is_none()

    def _publication_checker(self, pub_id) -> Optional[PublicationChecker]:
        return next((PublicationChecker(pub) for pub in self._publications if pub.id == pub_id), None)

    @deprecated(reason='It is very hard to debug an assertion fail. Prefer using publication(pub_id) or publications()')
    def assert_that_published_publications_are(self, *publications: Publication):
        assert_that(self._publications) \
            .is_length(len(publications)) \
            .contains(*publications)

    def assert_that_no_publication_is_published(self):
        """Assert that no publication have been published."""
        assert_that(self._publications).is_empty()

    def update_rights(self, rights_updates: RightsUpdates):
        for update in rights_updates.updates:
            self._rights_update[update.pub_id] = update.rights

    @deprecated(reason='Prefer using content access right rules than setting rights by publication.')
    def rights_update(self, publication_id: str) -> RightsChecker:
        """Return a checker on right update.
        If multiple right updates concern the same Publication, it only returns the last one.

        :param publication_id: ID of Publication concerned by the RightsUpdate.
        :return A RightsChecker to make asserts on the Rights.
        :raises:
            AssertionError: No Publication with this ID has been rights updated."""
        assert_that(self._rights_update).contains_key(publication_id)
        return RightsChecker(self._rights_update[publication_id])

    @deprecated(reason='It is very hard to debug an assertion fail. Prefer using rights_update(pub_id)')
    def assert_that_rights_update_are(self, rights_updates: RightsUpdates):
        given_rights = {u.pub_id: u.rights for u in rights_updates.updates}
        assert self._rights_update == given_rights

    def update_metadata(self, meta_updates: MetadataUpdates):
        for update in meta_updates.updates:
            self._meta_update[update.pub_id] = update

    @deprecated(reason='It is very hard to debug an assertion fail. '
                       'Prefer using metadata_update() or publication_metadata(pub_id)')
    def assert_that_metadata_update_are(self, meta_updates: MetadataUpdates):
        given_meta = {u.pub_id: u for u in meta_updates.updates}
        assert self._meta_update == given_meta

    def publication_metadata(self, publication_id: str) -> PublicationMetadataChecker:
        """Return a checker on the last metada update which concern the Publication.

        :param publication_id: ID of the updated Publication.
        :return A PublicationMetadataChecker to make asserts on the PublicationMetadata.
        :raises:
            AssertionError: No Publication with this ID has been updated"""
        assert_that(self._meta_update).contains_key(publication_id)
        return PublicationMetadataChecker(self._meta_update[publication_id])

    def update_attachments(self, attachments_updates: AttachmentsUpdate):
        self._attachments_update = attachments_updates

    def attachments(self) -> List[AttachmentChecker]:
        """Return checkers on all updated Attachments."""
        return [AttachmentChecker(a) for a in self._attachments_update.attachments]

    def attachment(self, attachment_id: str) -> AttachmentChecker:
        """Return a checker on a specific Attachment.

        :param attachment_id: ID of the Attachment to check.
        :return AttachmentChecker to make assert on the Attachment.
        :raises:
            AssertionError: No Attachment with this ID has been published."""
        attachment = (AttachmentChecker(a) for a in self._attachments_update.attachments if a.id == attachment_id)
        attachment = next(attachment, None)
        assert_that(attachment) \
            .described_as('{} not found in asynchronous attachment list: {}'
                          .format(attachment_id, [a.id for a in self._attachments_update.attachments])) \
            .is_not_none()
        return attachment

    def attach_commands(self) -> List[AttachCommandChecker]:
        """Return checkers on all sent AttachCommand."""
        return [AttachCommandChecker(a) for a in self._attachments_update.attach]

    # pylint: disable=inconsistent-return-statements
    def attach_command(self, pub_id: str, attachment_id: str) -> AttachCommandChecker:
        """Return a checker on an AttachCommand which link a specific Attachment with a specific Publication.

        :param pub_id: ID of the linked Publication.
        :param attachment_id: ID of the linked Attachment.
        :return AttachCommandChecker to make assert on the AttachCommand.
        :raises:
            AssertionError: No AttachCommand links this Publication and this Attachment."""
        for a in self._attachments_update.attach:
            if a.attachment_id == attachment_id and a.pub_id == pub_id:
                return AttachCommandChecker(a)
        fail('(pub_id={}, attachment_id={}) not found in asynchronous attach command list: {}'
             .format(pub_id, attachment_id, self._attachments_update.attach))

    def detach_commands(self) -> List[DetachCommandChecker]:
        """Return checkers on all snet DetachCommand."""
        return [DetachCommandChecker(a) for a in self._attachments_update.attach]

    # pylint: disable=inconsistent-return-statements
    def detach_command(self, pub_id: str, attachment_id: str) -> DetachCommandChecker:
        """Return a checker on an DetachCommand which detach a specific Attachment and a specific Publication.

        :param pub_id: ID of the Publication.
        :param attachment_id: ID of the detached Attachment.
        :return DetachCommandChecker to make assert on the DetachCommand.
        :raises:
            AssertionError: No DetachCommand detach this Publication and this Attachment."""
        for d in self._attachments_update.detach:
            if d.attachment_id == attachment_id and d.pub_id == pub_id:
                return DetachCommandChecker(d)
        fail('(pub_id={}, attachment_id={}) not found in asynchronous detach command list: {}'
             .format(pub_id, attachment_id, self._attachments_update.detach))

    def delete(self, publication_ids: List[str]):
        self._deletions.extend(publication_ids)

    def assert_that_deleted_publications_are(self, *publication_ids: str):
        """Check that Publications have been removed.

        :param publication_ids: ID of expected removed Publications."""
        assert_that(self._deletions) \
            .is_length(len(publication_ids)) \
            .contains(*publication_ids)

    def delete_all(self):
        self._delete_all = True

    def assert_that_delete_all_has_been_called(self):
        """Check if delete_all() was called."""
        assert_that(self._delete_all).is_true()

    def assert_has_no_delete(self):
        """Check that there was no Publication deletion."""
        assert_that(self._deletions).is_empty()
