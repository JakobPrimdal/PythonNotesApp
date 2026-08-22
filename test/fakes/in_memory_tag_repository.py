from typing import Optional
from uuid import UUID

from domain.Tag import Tag


class InMemoryTagRepository:
    """
    InMemoryTagRepository is a simple implementation of ITagRepository.

    Used only in tests, to test the application-layer's use cases without a real DB.
    Acts as a real repository (data is there, and query works - however, only in memory)
    """

    def __init__(self) -> None:
        self._tags: dict[UUID, Tag] = {}

    def get_by_uuid(self, tag_uuid: UUID) -> Optional[Tag]:
        return self._tags.get(tag_uuid)

    def get_all(self) -> list[Tag]:
        return list(self._tags.values())

    def save(self, tag: Tag) -> None:
        self._tags[tag.id] = tag

    def delete(self, tag_uuid: UUID) -> None:
        if tag_uuid in self._tags:
            del self._tags[tag_uuid]
