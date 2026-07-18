from uuid import UUID

from domain.errors.NoteNotFoundError import NoteNotFoundError
from domain.interfaces.INoteRepository import INoteRepository


class DeleteNote:
    def __init__(self, note_repository: INoteRepository) -> None:
        self._note_repository = note_repository

    def execute(self, note_uuid: UUID) -> None:
        note = self._note_repository.get_by_uuid(note_uuid)
        if note is None:
            raise NoteNotFoundError(f"Note with uuid {note_uuid} not found")
        self._note_repository.delete(note_uuid)