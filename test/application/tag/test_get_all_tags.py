from application.use_cases.tag.CreateTag import CreateTag
from application.use_cases.tag.GetAllTags import GetAllTags
from test.fakes.in_memory_tag_repository import InMemoryTagRepository


def test_returns_empty_list_when_no_tags_exist():
    # Arrange
    repository = InMemoryTagRepository()
    use_case = GetAllTags(tag_repository=repository)

    # Act
    result = use_case.execute()

    # Assert
    assert result == []


def test_returns_all_created_tags():
    # Arrange
    repository = InMemoryTagRepository()
    create = CreateTag(tag_repository=repository)
    create.execute("Work")
    create.execute("Personal")
    use_case = GetAllTags(tag_repository=repository)

    # Act
    result = use_case.execute()

    # Assert
    assert len(result) == 2
    assert {tag.name for tag in result} == {"work", "personal"}