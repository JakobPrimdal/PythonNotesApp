from typing import Optional
from uuid import UUID

from domain.interfaces.INoteRepository import INoteRepository
from domain.Note import Note


class GetNoteByUUID:

    def __init__(self, note_repository: INoteRepository) -> None:
        self._note_repository = note_repository

    def execute(self, note_uuid: UUID) -> Optional[Note]:
        note = self._note_repository.get_by_uuid(note_uuid)
        return note

