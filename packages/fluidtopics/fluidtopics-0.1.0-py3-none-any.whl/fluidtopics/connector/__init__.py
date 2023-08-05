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

from fluidtopics.connector.client import Client, RemoteClient, Authentication, Base64Authentication, LoginAuthentication
from fluidtopics.connector.helpers.attachment_update_checker import AttachCommandChecker, DetachCommandChecker, \
    AttachmentChecker
from fluidtopics.connector.helpers.fake_client import FakeClient
from fluidtopics.connector.helpers.metadata_inheritor import MetadataInheritor
from fluidtopics.connector.helpers.metadata_update_checker import PublicationMetadataChecker
from fluidtopics.connector.helpers.publication_checker import PublicationChecker, MetadataChecker, TopicChecker, \
    AttachmentLinkChecker, ResourceChecker, RightsChecker
from fluidtopics.connector.model.attachment_update import Attachment, AttachCommand, DetachCommand, AttachmentsUpdate, \
    AttachCommandBuilder, DetachCommandBuilder, AttachmentBuilder, AttachmentsUpdateBuilder, InvalidAttachment, \
    InvalidCommand
from fluidtopics.connector.model.body import Body, ExpandingBlock, FT_LINK_TYPE_ATTR, FT_LINK_TYPE_BASE_ID, \
    EXPANDING_BLOCK_LINK_CLASS, EXPANDING_BLOCK_CONTENT_CLASS, EXPANDING_BLOCK_INLINE_CONTENT_CLASS
from fluidtopics.connector.model.metadata import SemanticMetadata, OpenMode, MetadataType, Snapshot, Journal, \
    Metadata, DEFAULT_PRODUCER
from fluidtopics.connector.model.metadata_update import MetadataUpdates, PublicationMetadata, MetadataAction
from fluidtopics.connector.model.publication import Publication, AttachmentLink, EditorialType, StructuredContent, \
    UnstructuredContent, TocNode, PublicationBuilder, InvalidPublication
from fluidtopics.connector.model.resource import Resource, InvalidResource, ResourceBuilder
from fluidtopics.connector.model.right import AccessLevel, Rights
from fluidtopics.connector.model.right_update import RightsUpdates, PublicationRights
from fluidtopics.connector.model.topic import Topic, TopicBuilder, InvalidTopic

__all__ = [
    'DEFAULT_PRODUCER',
    'EXPANDING_BLOCK_CONTENT_CLASS',
    'EXPANDING_BLOCK_INLINE_CONTENT_CLASS',
    'EXPANDING_BLOCK_LINK_CLASS',
    'FT_LINK_TYPE_ATTR',
    'FT_LINK_TYPE_BASE_ID',
    'AccessLevel',
    'AttachCommand',
    'AttachCommandBuilder',
    'AttachCommandChecker',
    'Attachment',
    'AttachmentBuilder',
    'AttachmentChecker',
    'AttachmentLink',
    'AttachmentLinkChecker',
    'AttachmentsUpdate',
    'AttachmentsUpdateBuilder',
    'Base64Authentication',
    'Body',
    'Client',
    'DetachCommand',
    'DetachCommandBuilder',
    'DetachCommandChecker',
    'EditorialType',
    'ExpandingBlock',
    'FakeClient',
    'InvalidAttachment',
    'InvalidCommand',
    'InvalidPublication',
    'InvalidResource',
    'InvalidTopic',
    'Journal',
    'LoginAuthentication',
    'Metadata',
    'MetadataChecker',
    'MetadataAction',
    'MetadataInheritor',
    'MetadataType',
    'MetadataUpdates',
    'OpenMode',
    'Publication',
    'PublicationBuilder',
    'PublicationChecker',
    'PublicationMetadata',
    'PublicationMetadataChecker',
    'PublicationRights',
    'RemoteClient',
    'Resource',
    'ResourceBuilder',
    'ResourceChecker',
    'Rights',
    'RightsChecker',
    'RightsUpdates',
    'SemanticMetadata',
    'Snapshot',
    'StructuredContent',
    'TocNode',
    'Topic',
    'TopicBuilder',
    'TopicChecker',
    'UnstructuredContent',
]
