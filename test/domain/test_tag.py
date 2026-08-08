import pytest

from domain.Tag import Tag


def test_create_tag_with_name_succeeds():
    # Arrange & Act
    tag = Tag.create("python")

    # Assert
    assert tag.id is not None
    assert tag.name == "python"
    assert isinstance(tag, Tag)


def test_create_tag_strips_and_lowercases_name():
    # Arrange & Act
    tag = Tag.create("  Python  ")

    # Assert
    assert tag.name == "python"


def test_create_tag_with_empty_name_raises_error():
    # Act & Assert
    with pytest.raises(ValueError):
        Tag.create("")


def test_create_tag_with_only_whitespace_raises_error():
    # Act & Assert
    with pytest.raises(ValueError):
        Tag.create("   ")


def test_create_tag_with_max_length_name_succeeds():
    # Arrange
    max_length_name = "a" * Tag.MAX_LENGTH

    # Act
    tag = Tag.create(max_length_name)

    # Assert
    assert tag.name == max_length_name


def test_create_tag_with_too_long_name_raises_error():
    # Arrange
    too_long_name = "a" * (Tag.MAX_LENGTH + 1)

    # Act & Assert
    with pytest.raises(ValueError):
        Tag.create(too_long_name)


def test_rename_tag_succeeds():
    # Arrange
    tag = Tag.create("python")

    # Act
    tag.rename("java")

    # Assert
    assert tag.name == "java"


def test_rename_tag_strips_and_lowercases_name():
    # Arrange
    tag = Tag.create("python")

    # Act
    tag.rename("  Java  ")

    # Assert
    assert tag.name == "java"


def test_rename_tag_to_empty_name_raises_error():
    # Arrange
    tag = Tag.create("python")

    # Act & Assert
    with pytest.raises(ValueError):
        tag.rename("")


def test_rename_tag_to_only_whitespace_raises_error():
    # Arrange
    tag = Tag.create("python")

    # Act & Assert
    with pytest.raises(ValueError):
        tag.rename("   ")


def test_rename_tag_to_too_long_name_raises_error():
    # Arrange
    tag = Tag.create("python")
    too_long_name = "a" * (Tag.MAX_LENGTH + 1)

    # Act & Assert
    with pytest.raises(ValueError):
        tag.rename(too_long_name)


def test_two_tags_with_same_id_are_equal():
    # Arrange
    tag = Tag.create("python")
    same_tag_reference = tag

    # Act & Assert
    assert tag == same_tag_reference


def test_two_different_tags_are_not_equal_even_with_same_name():
    # Arrange
    tag_a = Tag.create("python")
    tag_b = Tag.create("python")

    # Act & Assert
    assert tag_a != tag_b


def test_renamed_tag_is_still_equal_to_itself():
    # Arrange
    tag = Tag.create("python")
    tag_id_before_rename = tag.id

    # Act
    tag.rename("java")

    # Assert
    assert tag.id == tag_id_before_rename