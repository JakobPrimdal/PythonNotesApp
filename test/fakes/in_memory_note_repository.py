from typing import Optional
from uuid import UUID

from domain.Note import Note


class InMemoryNoteRepository:
    """
    InMemoryNoteRepository is a simple implementation of INoteRepository.

    Used only in tests, to test the application-layer's use cases without a real DB.
    Acts as a real repository (data is there, and query works - however, only in memory)
    """

    def __init__(self) -> None:
        self._notes: dict[UUID, Note] = {}

    def get_by_uuid(self, note_uuid: UUID) -> Optional[Note]:
        return self._notes.get(note_uuid)

    def get_all(self) -> list[Note]:
        return list(self._notes.values())

    def get_by_folder_id(self, folder_uuid: UUID) -> list[Note]:
        notes = [
            note for note in self._notes.values() if note.folder_id == folder_uuid
        ]
        return notes

    def save(self, note: Note) -> None:
        self._notes[note.id] = note

    def delete(self, note_uuid: UUID) -> None:
        if note_uuid in self._notes:
            del self._notes[note_uuid]