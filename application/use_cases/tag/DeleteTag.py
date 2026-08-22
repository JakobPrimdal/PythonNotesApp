from uuid import UUID

from domain.errors.TagNotFoundError import TagNotFoundError
from domain.interfaces.INoteRepository import INoteRepository
from domain.interfaces.ITagRepository import ITagRepository


class DeleteTag:
    def __init__(self, tag_repository: ITagRepository, note_repository: INoteRepository) -> None:
        self._tag_repository = tag_repository
        self._note_repository = note_repository

    def execute(self, tag_uuid: UUID) -> None:
        tag = self._tag_repository.get_by_uuid(tag_uuid)
        if tag is None:
            raise TagNotFoundError(f"Tag with uuid {tag_uuid} not found")

        notes_with_tag = [n for n in self._note_repository.get_all() if tag_uuid in n.tag_ids]
        for note in notes_with_tag:
            note.discard_tag_reference(tag_uuid)
            self._note_repository.save(note)

        self._tag_repository.delete(tag_uuid)
