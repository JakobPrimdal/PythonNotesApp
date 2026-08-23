from uuid import uuid4

import pytest

from application.use_cases.tag.CreateTag import CreateTag
from application.use_cases.tag.GetTagByUUID import GetTagByUUID
from domain.errors.TagNotFoundError import TagNotFoundError
from test.fakes.in_memory_tag_repository import InMemoryTagRepository


def test_returns_tag_when_it_exists():
    # Arrange
    repository = InMemoryTagRepository()
    tag = CreateTag(tag_repository=repository).execute("Work")
    use_case = GetTagByUUID(tag_repository=repository)

    # Act
    result = use_case.execute(tag.id)

    # Assert
    assert result is not None
    assert result.name == "work"


def test_returns_none_when_tag_does_not_exist():
    # Arrange
    repository = InMemoryTagRepository()
    use_case = GetTagByUUID(tag_repository=repository)

    # Act & Assert
    with pytest.raises(TagNotFoundError):
        use_case.execute(uuid4())
