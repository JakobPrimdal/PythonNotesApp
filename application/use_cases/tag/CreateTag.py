from domain.Tag import Tag
from domain.errors.DuplicateTagNameError import DuplicateTagNameError
from domain.interfaces.ITagRepository import ITagRepository


class CreateTag:
    """
    Use case: Create a new tag

    Orchestras domain entity - Tote - and persistence - ITagRepository,
    but does not hold any business logic or rules
    """

    def __init__(self, tag_repository: ITagRepository) -> None:
        self._tag_repository = tag_repository

    def execute(self, name: str) -> Tag:
        if any (tag.name == name.lower().strip() for tag in self._tag_repository.get_all()):
            raise DuplicateTagNameError(f"Tag with name {name} already exists")
        tag = Tag.create(name=name)
        self._tag_repository.save(tag)
        return tag