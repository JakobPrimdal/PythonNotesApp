from uuid import uuid4

from domain.Folder import Folder
from test.fakes.in_memory_folder_repository import InMemoryFolderRepository


def test_save_and_get_by_id_returns_saved_folder():
    # Arrange
    repository: InMemoryFolderRepository = InMemoryFolderRepository()
    folder = Folder.create("Folder")

    # Act
    repository.save(folder)
    found_folder = repository.get_by_uuid(folder.id)

    # Assert
    assert found_folder is folder

def test_get_by_id_with_unknown_id_returns_none():
    # Arrange
    repository: InMemoryFolderRepository = InMemoryFolderRepository()

    # Act
    found_folder = repository.get_by_uuid(uuid4())

    # Assert
    assert found_folder is None

def test_get_all_returns_all_saved_folders():
    # Arrange
    repository: InMemoryFolderRepository = InMemoryFolderRepository()
    folder_a = Folder.create("FolderA")
    folder_b = Folder.create("FolderB")

    # Act
    repository.save(folder_a)
    repository.save(folder_b)

    # Assert
    result_ids = {folder.id for folder in repository.get_all()}
    assert result_ids == {folder_a.id, folder_b.id}

def test_delete_removes_folder():
    # Arrange
    repository: InMemoryFolderRepository = InMemoryFolderRepository()
    folder = Folder.create("Folder")
    repository.save(folder)

    # Act
    repository.delete(folder.id)

    # Assert
    assert repository.get_by_uuid(folder.id) is None

def test_delete_unknown_id_does_not_raise_error():
    # Arrange
    repository: InMemoryFolderRepository = InMemoryFolderRepository()

    # Act & Assert (unknown uuid should not throw any exceptions)
    repository.delete(uuid4())