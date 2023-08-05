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

from autovalue import autovalue

from fluidtopics.connector.model.attachment_update import AttachmentsUpdate, Attachment, AttachCommand, DetachCommand


@autovalue
class FsonAttachment:
    def __init__(self, id: str = None, filename: str = None, title: str = None,
                 mime_type: str = None, content: str = None, url: str = None,
                 source_id: str = None, khub_id: str = None, file_path: str = None):
        self.id = id
        self.source_id = source_id
        self.khub_id = khub_id
        self.filename = filename
        self.title = title
        self.mime_type = mime_type
        self.file_path = file_path
        self.content = content
        self.url = url


@autovalue
class FsonAttachCommand:
    def __init__(self, pub_id: str = None, attachment_id: str = None,
                 tags: List[str] = None, title: str = None, insert_at: int = None,
                 pub_khub_id: str = None, attachment_source_id: str = None,
                 attachment_khub_id: str = None):
        self.pub_id = pub_id
        self.pub_khub_id = pub_khub_id
        self.attachment_id = attachment_id
        self.attachment_source_id = attachment_source_id
        self.attachment_khub_id = attachment_khub_id
        self.tags = tags if tags is not None else list()
        self.title = title
        self.insert_at = insert_at


@autovalue
class FsonDetachCommand:
    def __init__(self, pub_id: str = None, attachment_id: str = None,
                 pub_khub_id: str = None, attachment_source_id: str = None,
                 attachment_khub_id: str = None):
        self.pub_id = pub_id
        self.pub_khub_id = pub_khub_id
        self.attachment_id = attachment_id
        self.attachment_source_id = attachment_source_id
        self.attachment_khub_id = attachment_khub_id


@autovalue
class FsonAttachmentsUpdate:
    def __init__(self, attachments: List[FsonAttachment],
                 attach: List[FsonAttachCommand],
                 detach: List[FsonDetachCommand]):
        self.attachments = attachments
        self.attach = attach
        self.detach = detach


class AttachmentUpdateConverter:
    def convert_attachments_update(self, update: AttachmentsUpdate) -> FsonAttachmentsUpdate:
        attachments = [self._convert_attachment(a) for a in update.attachments]
        attach = [self._convert_attach(a) for a in update.attach]
        detach = [self._convert_detach(a) for a in update.detach]
        return FsonAttachmentsUpdate(attachments, attach, detach)

    def _convert_attachment(self, attachment: Attachment) -> FsonAttachment:
        content = None
        if attachment.content is not None:
            content = base64.b64encode(attachment.content).decode('utf-8')
        return FsonAttachment(
            attachment.id,
            attachment.filename,
            attachment.title,
            attachment.mime_type,
            content,
            attachment.url,
            attachment.source_id,
            attachment.khub_id,
            attachment.file_path)

    def _convert_attach(self, attach: AttachCommand) -> FsonAttachCommand:
        return FsonAttachCommand(
            attach.pub_id,
            attach.attachment_id,
            attach.tags,
            attach.title,
            attach.insert_at,
            attach.pub_khub_id,
            attach.attachment_source_id,
            attach.attachment_khub_id)

    def _convert_detach(self, detach: DetachCommand) -> FsonDetachCommand:
        return FsonDetachCommand(
            detach.pub_id,
            detach.attachment_id,
            detach.pub_khub_id,
            detach.attachment_source_id,
            detach.attachment_khub_id)
