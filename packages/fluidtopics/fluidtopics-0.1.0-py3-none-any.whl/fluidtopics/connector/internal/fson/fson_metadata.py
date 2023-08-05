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
from typing import List, Optional

from autovalue import autovalue

from fluidtopics.connector.model.metadata import Metadata, MetadataType, Journal, Snapshot


class FsonMetadataType(Enum):
    STRING = 1
    STRING_TREE = 2


@autovalue
class FsonSnapshot:
    def __init__(self, mtype: FsonMetadataType, key: str,
                 values: List[List[str]], producer: str, comment: str = None):
        self.mtype = mtype
        self.key = key
        self.values = values
        self.producer = producer
        self.comment = comment


@autovalue
class FsonJournal:
    def __init__(self, snapshots: List[FsonSnapshot]):
        self.snapshots = snapshots

    def add(self, snapshot: FsonSnapshot) -> 'FsonJournal':
        snapshots = self.snapshots.copy()
        snapshots.append(snapshot)
        return FsonJournal(snapshots)

    @classmethod
    def empty(cls) -> 'FsonJournal':
        return cls([])


@autovalue
class FsonMetadata:
    def __init__(self, key: str, producer: str, values: List[str] = None,
                 hierarchical_values: List[List[str]] = None,
                 comment: str = None, journal: FsonJournal = None):
        self.key = key
        self.producer = producer
        self.values = values
        self.hierarchical_values = hierarchical_values
        self.comment = comment
        self.journal = journal if journal is not None else FsonJournal.empty()


class MetadataConverter:
    def convert_metadata_list(self, metadata: Optional[List[Metadata]]) -> Optional[List[FsonMetadata]]:
        if metadata is None:
            return None
        return [self.convert_metadata(m) for m in metadata]

    def convert_metadata(self, meta: Metadata) -> FsonMetadata:
        journal = self._convert_journal(meta.journal)
        values = tree_values = None
        if meta.type == MetadataType.STRING:
            values = list(sorted(x[0] for x in meta.values))
        else:
            tree_values = list(sorted(list(value) for value in meta.values))
        return FsonMetadata(meta.key, meta.producer, values, tree_values, meta.comment, journal)

    def _convert_journal(self, journal: Journal) -> FsonJournal:
        snaps = [self._convert_snapshot(snap) for snap in journal.snapshots]
        return FsonJournal(snaps)

    def _convert_snapshot(self, snapshot: Snapshot) -> FsonSnapshot:
        values = [list(value) for value in snapshot.values]
        mtype = FsonMetadataType[snapshot.mtype.name]
        return FsonSnapshot(mtype, snapshot.key, values, snapshot.producer,
                            snapshot.comment)
