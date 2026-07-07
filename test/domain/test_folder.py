import pytest

from domain.Folder import Folder


def test__create_folder_with_name_succeeds():
    # Arrange
    folder = Folder.create(name="name")

    # Assert
    assert folder.id is not None
    assert folder.name == "name"
    assert folder.created_at is not None
    assert isinstance(folder, Folder)

def test_create_folder_with_empty_name_raises_error():
    # Assert
    with pytest.raises(ValueError):
        folder = Folder.create("")

def test_create_folder_with_only_whitespace_name_raises_error():
    # Assert
    with pytest.raises(ValueError):
        folder = Folder.create("   ")

def test_create_folder_with_max_length_name_succeeds():
    # Arrange
    max_length_name = "a" * Folder.MAX_NAME_LENGTH

    # Act
    folder = Folder.create(name=max_length_name)

    # Assert
    assert folder.name == max_length_name

def test_create_folder_with_too_long_name_raises_error():
    # Arrange
    too_long_name = "a" * (Folder.MAX_NAME_LENGTH+1)

    # Act & Assert
    with pytest.raises(ValueError):
        folder = Folder.create(too_long_name)

def test_rename_folder_name_succeeds():
    # Arrange
    folder = Folder.create(name="name")

    # Act
    folder.rename("new_name")

    # Assert
    assert folder.name == "new_name"

def test_rename_folder_to_empty_name_raises_error():
    # Arrange
    folder = Folder.create(name="name")

    # Act & Assert
    with pytest.raises(ValueError):
        folder.rename("")

def test_rename_folder_to_only_whitespace_name_raises_error():
    # Arrange
    folder = Folder.create(name="name")

    # Act & Assert
    with pytest.raises(ValueError):
        folder.rename("   ")

def test_rename_folder_to_too_long_name_raises_error():
    # Arrange
    folder = Folder.create(name="name")
    too_long_name = "a" * (Folder.MAX_NAME_LENGTH+1)

    # Act & Assert
    with pytest.raises(ValueError):
        folder.rename(too_long_name)
