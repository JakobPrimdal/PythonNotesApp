from typing import runtime_checkable, Protocol, Optional
from uuid import UUID

from domain.Tag import Tag


@runtime_checkable
class ITagRepository(Protocol):
    def get_by_uuid(self, tag_uuid: UUID) -> Optional[Tag]:
        ...

    def get_all(self) -> list[Tag]:
        ...

    def save(self, tag: Tag) -> Optional[Tag]:
        ...

    def delete(self, tag_uuid: UUID) -> Optional[Tag]:
        ...