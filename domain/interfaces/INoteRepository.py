from typing import runtime_checkable, Protocol, Optional
from uuid import UUID

from domain.Note import Note


@runtime_checkable
class INoteRepository(Protocol):
    def get_by_uuid(self, note_uuid: UUID) -> Optional[Note]:
        ...

    def get_all(self) -> list[Note]:
        ...

    def get_by_folder_id(self, folder_uuid: UUID) -> list[Note]:
        ...

    def save(self, note: Note) -> None:
        ...

    def delete(self, note_uuid: UUID) -> None:
        ...