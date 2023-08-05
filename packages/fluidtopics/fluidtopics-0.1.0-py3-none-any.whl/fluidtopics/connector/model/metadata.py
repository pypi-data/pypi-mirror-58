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

import re
from enum import Enum
from typing import Set, Tuple, Optional, List, Union

from autovalue import autovalue

from fluidtopics.connector.internal.utils import Utils

DEFAULT_PRODUCER = 'Data'


class SemanticMetadata:
    """List of semantic metadata IDs."""
    TITLE = 'ft:title'
    LOCALE = 'ft:locale'
    BASE_ID = 'ft:baseId'
    CLUSTER_ID = 'ft:clusterId'
    OPEN_MODE = 'ft:openMode'
    ORIGIN_URL = 'ft:originUrl'
    EDITORIAL_TYPE = 'ft:editorialType'
    LAST_EDITION = 'ft:lastEdition'
    DESCRIPTION = 'ft:description'
    PRETTY_URL = 'ft:prettyUrl'

    values = {TITLE, LOCALE, BASE_ID, CLUSTER_ID, OPEN_MODE, ORIGIN_URL,
              EDITORIAL_TYPE, LAST_EDITION, DESCRIPTION, PRETTY_URL}


class OpenMode:
    """Possible values for ft:openMode metadata."""
    FLUIDTOPICS = 'fluidtopics'
    EXTERNAL = 'external'

    @staticmethod
    def is_valid(value: str) -> bool:
        """Check if a value is a correct ft:openMode value."""
        return value in (OpenMode.FLUIDTOPICS, OpenMode.EXTERNAL)


class MetadataType(Enum):
    """Define if the Metadata value is hierarchical or not."""
    STRING = 1
    STRING_TREE = 2


@autovalue
class Snapshot:
    """Snapshot of a Metadata state in the Journal.

    Prefer using Metadata.update() to build the Metadata journal than creating it
    manually."""
    def __init__(self, mtype: MetadataType, key: str,
                 values: Set[Tuple[str, ...]], producer: str,
                 comment: Optional[str] = None):
        self.mtype = mtype
        self.key = key
        self.values = values
        self.producer = producer
        self.comment = comment

    @staticmethod
    def from_meta(meta: 'Metadata') -> 'Snapshot':
        return Snapshot(meta.type, meta.key, meta.values, meta.producer,
                        meta.comment)


@autovalue
class Journal:
    """History of Metadata states.

    Prefer using Metadata.update() to build the Metadata journal than creating it
    manually."""
    def __init__(self, snapshots: List[Snapshot]):
        self.snapshots = snapshots

    def add(self, snapshot: Snapshot) -> 'Journal':
        """Create a new Journal from the current one with the new Snapshot."""
        snapshots = self.snapshots.copy()
        snapshots.append(snapshot)
        return Journal(snapshots)

    @staticmethod
    def empty() -> 'Journal':
        """Create an empty Journal."""
        return Journal([])


@autovalue
class Metadata:
    """A Metadata of a Topic or a Publication.

    A Metadata have associate a key with one or more values.
    If it is a String Metadata, values looks like:
        {(value1,), (value2,)}
    If it is a StringTree Metadata, values looks like:
        {(hierarchical, value1), (hierarchical, value2), (value3,)}

    producer and comment are used in the metadata journal."""
    _date_regex = re.compile('^[0-9]{4}-[0-9]{2}-[0-9]{2}$')

    def __init__(self, type: MetadataType, key: str,
                 values: Set[Tuple[str, ...]], producer: str = DEFAULT_PRODUCER,
                 comment: Optional[str] = None, journal: Journal = None):
        self.type = type
        self.key = key
        self.values = values
        self.producer = producer
        self.comment = comment
        self.journal = journal if journal is not None else Journal.empty()

    def is_equivalent_to(self, other: 'Metadata') -> bool:
        """Compare two Metadata ignoring their Journal."""
        return other is not None \
            and self.type == other.type \
            and self.key == other.key \
            and self.values == other.values \
            and self.producer == other.producer

    @property
    def first_value(self) -> Optional[str]:
        """Helper to get the value of a String Metadata with one value.

        :return first part of the first value of the Metadata or None if there
                is no value."""
        try:
            return next(iter(next(iter(self.values))))
        except StopIteration:
            return None

    @property
    def first_hierarchical_value(self) -> Optional[List[str]]:
        """Helper to get the value of a StringTree Metadata with one value.

        :return first hierarchical value of the Metadata or None if there is
                no value."""
        try:
            return list(next(iter(self.values)))
        except StopIteration:
            return None

    @property
    def string_values(self) -> List[str]:
        """Helper to get values of a String Metadata.

        :return flat list of values of the Metadata or empty list if there is
                no value."""
        return [v[0] for v in self.values if v]

    @staticmethod
    def string(key: str, values: Union[List[str], Set[str]],
               producer: str = DEFAULT_PRODUCER,
               comment: str = None) -> 'Metadata':
        """Create a String Metadata."""
        values = {(value,) for value in values}
        return Metadata(MetadataType.STRING, key, values, producer, comment)

    @staticmethod
    def string_tree(key: str,
                    breadcrumbs: Union[List[List[str]], Set[Tuple[str, ...]]],
                    producer: str = DEFAULT_PRODUCER,
                    comment: str = None) -> 'Metadata':
        """Create a StringTree Metadata."""
        values = {tuple(value) for value in breadcrumbs}
        meta_type = MetadataType.STRING_TREE
        return Metadata(meta_type, key, values, producer, comment)

    @staticmethod
    def title(value: str, producer: str = DEFAULT_PRODUCER, comment: str = None) -> 'Metadata':
        """Create a {} Metadata.""".format(SemanticMetadata.TITLE)
        return Metadata.string(SemanticMetadata.TITLE, {value}, producer, comment)

    @staticmethod
    def last_edition(value: str, producer: str = DEFAULT_PRODUCER, comment: str = None) -> 'Metadata':
        """Create a {} Metadata.

        The value should match the format YYYY-MM-DD""".format(SemanticMetadata.LAST_EDITION)
        if not Metadata._date_regex.match(value):
            raise ValueError('Invalid last edition date "{}", '
                             'expected format "YYYY-MM-DD"'.format(value))
        return Metadata.string(SemanticMetadata.LAST_EDITION, {value}, producer, comment)

    @staticmethod
    def locale(value: str, producer: str = DEFAULT_PRODUCER, comment: str = None) -> 'Metadata':
        """Create a {} Metadata.

        The value should be a valid ISO code.""".format(SemanticMetadata.LOCALE)
        value = Utils.parse_ietf_language_tag(value)
        return Metadata.string(SemanticMetadata.LOCALE, {value}, producer, comment)

    @staticmethod
    def base_id(value: str, producer: str = DEFAULT_PRODUCER, comment: str = None) -> 'Metadata':
        """Create a {} Metadata.""".format(SemanticMetadata.BASE_ID)
        return Metadata.string(SemanticMetadata.BASE_ID, {value}, producer, comment)

    @staticmethod
    def cluster_id(value: str, producer: str = DEFAULT_PRODUCER, comment: str = None) -> 'Metadata':
        """Create a {} Metadata.""".format(SemanticMetadata.CLUSTER_ID)
        return Metadata.string(SemanticMetadata.CLUSTER_ID, {value}, producer, comment)

    @staticmethod
    def open_mode(value: str, producer: str = DEFAULT_PRODUCER, comment: str = None) -> 'Metadata':
        """Create a {} Metadata.

        The value should be a valid OpenMode.""".format(SemanticMetadata.OPEN_MODE)
        if not OpenMode.is_valid(value):
            raise ValueError('Invalid open mode "{}"'.format(value))
        return Metadata.string(SemanticMetadata.OPEN_MODE, {value}, producer, comment)

    @staticmethod
    def origin_url(value: str, producer: str = DEFAULT_PRODUCER, comment: str = None) -> 'Metadata':
        """Create a {} Metadata.""".format(SemanticMetadata.ORIGIN_URL)
        return Metadata.string(SemanticMetadata.ORIGIN_URL, {value}, producer, comment)

    @staticmethod
    def description(value: str, producer: str = DEFAULT_PRODUCER, comment: str = None) -> 'Metadata':
        """Create a {} Metadata.""".format(SemanticMetadata.DESCRIPTION)
        return Metadata.string(SemanticMetadata.DESCRIPTION, {value}, producer, comment)

    @staticmethod
    def pretty_url(value: str, producer: str = DEFAULT_PRODUCER, comment: str = None) -> 'Metadata':
        """Create a {} Metadata.""".format(SemanticMetadata.PRETTY_URL)
        return Metadata.string(SemanticMetadata.PRETTY_URL, {value}, producer, comment)

    def update(self, meta: 'Metadata') -> 'Metadata':
        """Update the metadata state (type, key, values).

        It is advised to use this method to update any aspect of the metadata
        (type, key, values). Use producer and comment of the meta param to
        explain why this change is made.
        Example:
            old = Metadata.string('version', ['v1.0'])
            new = Metadata.string('version', ['1.0'], 'NORMALIZER', 'Normalize version')
            updated = old.update(new)

        :param meta: New state of the Metadata.
        :return: Metadata with the meta state, and a Journal which contains
                 previous states of the current Metadata."""
        journal = self._update_journal()
        return Metadata(meta.type, meta.key, meta.values, meta.producer,
                        meta.comment, journal)

    def _update_journal(self) -> Journal:
        snapshot = Snapshot.from_meta(self)
        return self.journal.add(snapshot)
