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

from enum import Enum
from typing import List, Optional, Union

from autovalue import autovalue
from pynject import pynject

from fluidtopics.connector.internal.fson.fson_metadata import FsonMetadata, MetadataConverter
from fluidtopics.connector.internal.fson.fson_right import FsonRights, RightsConverter
from fluidtopics.connector.internal.fson.fson_section import FsonSection, SectionConverter
from fluidtopics.connector.model.publication import UnstructuredContent, EditorialType, StructuredContent, \
    Publication, AttachmentLink


@autovalue
class FsonAttachmentLink:
    def __init__(self, resource_id: str, tags: List[str], title: str = None):
        self.resource_id = resource_id
        self.tags = tags
        self.title = title


class FsonEditorialType(Enum):
    DEFAULT = 0
    ARTICLE = 1
    BOOK = 2


@autovalue
class FsonStructured:
    def __init__(self, sections: List[FsonSection], editorial_type: FsonEditorialType):
        self.sections = sections
        self.editorial_type = editorial_type


@autovalue
class FsonUnstructured:
    def __init__(self, resource_reference: str):
        self.resource_reference = resource_reference


@autovalue
class FsonContent:
    def __init__(self, structured: FsonStructured = None,
                 unstructured: FsonUnstructured = None):
        self.structured = structured
        self.unstructured = unstructured

    @staticmethod
    def structured_content(structured_content: FsonStructured) -> 'FsonContent':
        return FsonContent(structured=structured_content)

    @staticmethod
    def unstructured_content(resource_reference: str) -> 'FsonContent':
        return FsonContent(unstructured=FsonUnstructured(resource_reference))


@autovalue
class FsonPublication:
    def __init__(self, id: str,
                 content: FsonContent,
                 lang: str = None,
                 title: str = None,
                 rights: FsonRights = None,
                 metadata: List[FsonMetadata] = None,
                 base_id: str = None,
                 variant_selector: str = None,
                 attachments: List[FsonAttachmentLink] = None,
                 description: Optional[str] = None,
                 pretty_url: Optional[str] = None):
        self.id = id
        self.content = content
        self.lang = lang
        self.title = title
        self.rights = rights
        self.metadata = metadata
        self.base_id = base_id
        self.variant_selector = variant_selector
        self.attachments = attachments if attachments is not None else []
        self.description = description
        self.pretty_url = pretty_url

    @property
    def sections(self):
        return self.content.structured.sections


@pynject
class PublicationConverter:
    def __init__(self, section_converter: SectionConverter, metadata_converter: MetadataConverter,
                 rights_converter: RightsConverter):
        self._section_converter = section_converter
        self._metadata_converter = metadata_converter
        self._rights_converter = rights_converter

    def convert_unstructured_content(self, content: UnstructuredContent) -> FsonContent:
        return FsonContent.unstructured_content(content.resource_reference)

    def convert_editorial_type(self, editorial_type: EditorialType) -> FsonEditorialType:
        if editorial_type == EditorialType.BOOK:
            return FsonEditorialType.BOOK
        elif editorial_type == EditorialType.ARTICLE:
            return FsonEditorialType.ARTICLE
        elif editorial_type == EditorialType.DEFAULT:
            return FsonEditorialType.DEFAULT
        else:
            raise ValueError('Unknown {} "{}"'.format(EditorialType.__name__, editorial_type))

    def convert_structured_content(self, content: StructuredContent) -> FsonContent:
        editorial_type = self.convert_editorial_type(content.editorial_type)
        sections = self._section_converter.convert_toc(content.toc)
        return FsonContent.structured_content(FsonStructured(sections, editorial_type))

    def convert_to_content(self, content: Union[StructuredContent, UnstructuredContent]) \
            -> FsonContent:
        if isinstance(content, UnstructuredContent):
            return self.convert_unstructured_content(content)
        elif isinstance(content, StructuredContent):
            return self.convert_structured_content(content)
        else:
            raise TypeError('Unexpected publication content type: {}'.format(type(content)))

    def convert_publication(self, publication: Publication) -> FsonPublication:
        publication_metadata = self._metadata_converter.convert_metadata_list(publication.metadata)
        rights = self._rights_converter.convert_rights(publication.rights)
        content = self.convert_to_content(publication.content)
        attachments = self.convert_attachment_links(publication.attachments)
        return FsonPublication(
            id=publication.id,
            title=publication.title,
            lang=publication.lang,
            content=content,
            rights=rights,
            metadata=publication_metadata,
            base_id=publication.base_id,
            variant_selector=publication.variant_selector,
            attachments=attachments,
            description=publication.description,
            pretty_url=publication.pretty_url
        )

    def convert_attachment_links(self, attachments: List[AttachmentLink]) -> List[FsonAttachmentLink]:
        return [FsonAttachmentLink(a.resource_id, a.tags, a.title) for a in attachments]
