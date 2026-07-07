import dataclasses

import pytest

from domain.Tag import Tag


def test_create_tag_with_name_succeeds():
    # Arrange & Act
    tag = Tag("python")

    # Assert
    assert tag.name == "python"


def test_create_tag_strips_and_lowercases_name():
    # Arrange & Act
    tag = Tag("  Python  ")

    # Assert
    assert tag.name == "python"


def test_create_tag_with_empty_name_raises_error():
    # Act & Assert
    with pytest.raises(ValueError):
        Tag("")


def test_create_tag_with_only_whitespace_raises_error():
    # Act & Assert
    with pytest.raises(ValueError):
        Tag("   ")


def test_create_tag_with_too_long_name_raises_error():
    # Arrange
    too_long_name = "a" * (Tag.MAX_LENGTH + 1)

    # Act & Assert
    with pytest.raises(ValueError):
        Tag(too_long_name)


def test_two_tags_with_same_name_are_equal():
    # Arrange
    tag_a = Tag("python")
    tag_b = Tag("python")

    # Act & Assert
    assert tag_a == tag_b


def test_two_tags_with_different_casing_are_equal():
    # Arrange
    tag_a = Tag("python")
    tag_b = Tag("PYTHON")

    # Act & Assert
    assert tag_a == tag_b


def test_two_tags_with_different_names_are_not_equal():
    # Arrange
    tag_a = Tag("python")
    tag_b = Tag("java")

    # Act & Assert
    assert tag_a != tag_b


def test_tag_is_immutable():
    # Arrange
    tag = Tag("python")

    # Act & Assert
    with pytest.raises(dataclasses.FrozenInstanceError):
        tag.name = "java"