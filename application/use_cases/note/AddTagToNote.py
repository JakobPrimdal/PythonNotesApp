from uuid import UUID

from domain.errors.TagNotFoundError import TagNotFoundError
from domain.interfaces.INoteRepository import INoteRepository
from domain.interfaces.ITagRepository import ITagRepository
from domain.Note import Note
from domain.errors.NoteNotFoundError import NoteNotFoundError


class AddTagToNote:
    def __init__(self, note_repository: INoteRepository, tag_repository: ITagRepository) -> None:
        self._note_repository = note_repository
        self._tag_repository = tag_repository

    def execute(self, note_uuid: UUID, tag_uuid: UUID) -> Note:
        note = self._note_repository.get_by_uuid(note_uuid)
        if note is None:
            raise NoteNotFoundError(f"Note with uuid {note_uuid} not found")

        tag = self._tag_repository.get_by_uuid(tag_uuid)
        if tag is None:
            raise TagNotFoundError(f"Tag with uuid {tag_uuid} not found")

        note.add_tag(tag_uuid)
        self._note_repository.save(note)
        return note