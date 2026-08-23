from uuid import UUID

from domain.Tag import Tag
from domain.errors.DuplicateTagNameError import DuplicateTagNameError
from domain.errors.TagNotFoundError import TagNotFoundError
from domain.interfaces.ITagRepository import ITagRepository


class RenameTag:
    def __init__(self, tag_repository: ITagRepository) -> None:
        self._tag_repository = tag_repository

    def execute(self, tag_uuid: UUID, new_name: str) -> Tag:
        tag = self._tag_repository.get_by_uuid(tag_uuid)
        if tag is None:
            raise TagNotFoundError(f"Tag with uuid {tag_uuid} not found")

        if any (tag.name == new_name.lower().strip() for tag in self._tag_repository.get_all() if tag.id != tag_uuid):
            raise DuplicateTagNameError(f"Tag with name {new_name} already exists")

        tag.rename(new_name)
        self._tag_repository.save(tag)
        return tag
