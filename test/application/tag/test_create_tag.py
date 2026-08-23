import pytest

from application.use_cases.tag.CreateTag import CreateTag
from domain.errors.DuplicateTagNameError import DuplicateTagNameError
from test.fakes.in_memory_tag_repository import InMemoryTagRepository


def test_create_persists_tag():
    # Arrange
    repository = InMemoryTagRepository()
    use_case = CreateTag(tag_repository=repository)

    # Act
    result = use_case.execute("Work")

    # Assert
    assert result.name == "work"
    persisted_tag = repository.get_by_uuid(result.id)
    assert persisted_tag is not None
    assert persisted_tag.name == "work"


def test_raises_when_name_already_exists():
    # Arrange
    repository = InMemoryTagRepository()
    use_case = CreateTag(tag_repository=repository)
    use_case.execute("Work")

    # Act & Assert
    with pytest.raises(DuplicateTagNameError):
        use_case.execute("Work")


def test_raises_when_name_already_exists_with_different_casing():
    # Arrange
    repository = InMemoryTagRepository()
    use_case = CreateTag(tag_repository=repository)
    use_case.execute("work")

    # Act & Assert
    with pytest.raises(DuplicateTagNameError):
        use_case.execute("WORK")


def test_does_not_save_when_name_is_invalid():
    # Arrange
    repository = InMemoryTagRepository()
    use_case = CreateTag(tag_repository=repository)

    # Act & Assert
    with pytest.raises(ValueError):
        use_case.execute("")
    assert repository.get_all() == []