from uuid import UUID

from domain.interfaces.INoteRepository import INoteRepository
from domain.Note import Note
from domain.errors.NoteNotFoundError import NoteNotFoundError


class UpdateNoteTitle:
    def __init__(self, note_repository: INoteRepository) -> None:
        self._note_repository = note_repository

    def execute(self, note_uuid: UUID, new_title: str) -> Note:
        note = self._note_repository.get_by_uuid(note_uuid)
        if note is None:
            raise NoteNotFoundError(f"Note with uuid {note_uuid} not found")

        note.update_title(new_title)
        self._note_repository.save(note)
        return note
