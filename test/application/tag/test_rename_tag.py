import uuid

import pytest

from application.use_cases.tag.CreateTag import CreateTag
from application.use_cases.tag.RenameTag import RenameTag
from domain.errors.DuplicateTagNameError import DuplicateTagNameError
from domain.errors.TagNotFoundError import TagNotFoundError
from test.fakes.in_memory_tag_repository import InMemoryTagRepository


def test_rename_persists_new_name():
    # Arrange
    repository = InMemoryTagRepository()
    tag = CreateTag(tag_repository=repository).execute("Work")
    use_case = RenameTag(tag_repository=repository)

    # Act
    result = use_case.execute(tag.id, "Personal")

    # Assert
    assert result.name == "personal"
    persisted_tag = repository.get_by_uuid(tag.id)
    assert persisted_tag.name == "personal"


def test_raises_when_tag_does_not_exist():
    # Arrange
    repository = InMemoryTagRepository()
    use_case = RenameTag(tag_repository=repository)

    # Act & Assert
    with pytest.raises(TagNotFoundError):
        use_case.execute(uuid.uuid4(), "Personal")


def test_raises_when_new_name_already_exists():
    # Arrange
    repository = InMemoryTagRepository()
    create = CreateTag(tag_repository=repository)
    create.execute("Work")
    tag_to_rename = create.execute("Personal")
    use_case = RenameTag(tag_repository=repository)

    # Act & Assert
    with pytest.raises(DuplicateTagNameError):
        use_case.execute(tag_to_rename.id, "Work")


def test_can_rename_tag_to_its_own_current_name():
    # Arrange
    repository = InMemoryTagRepository()
    tag = CreateTag(tag_repository=repository).execute("Work")
    use_case = RenameTag(tag_repository=repository)

    # Act
    result = use_case.execute(tag.id, "Work")

    # Assert
    assert result.name == "work"