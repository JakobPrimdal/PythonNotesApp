from uuid import UUID

from domain.errors.TagNotFoundError import TagNotFoundError
from domain.interfaces.ITagRepository import ITagRepository


class GetTagByUUID:
    def __init__(self, tag_repository: ITagRepository):
        self._tag_repository = tag_repository

    def execute(self, tag_uuid: UUID):
        tag = self._tag_repository.get_by_uuid(tag_uuid)
        if tag is None:
            raise TagNotFoundError(f"Tag with {tag_uuid} uuid not found")
        return tag