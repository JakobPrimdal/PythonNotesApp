from uuid import uuid4

import pytest

from application.use_cases.folder.RenameFolder import RenameFolder
from domain.Folder import Folder
from domain.errors.DuplicateFolderNameError import DuplicateFolderNameError
from domain.errors.FolderNotFoundError import FolderNotFoundError
from test.fakes.in_memory_folder_repository import InMemoryFolderRepository


def test_rename_folder_succeeds():
    # Arrange
    repository = InMemoryFolderRepository()
    folder = Folder.create(name="folder")
    repository.save(folder=folder)
    use_case = RenameFolder(folder_repository=repository)

    # Act
    result = use_case.execute(folder_uuid=folder.id, new_name="new_name")

    # Assert
    assert result.name == "new_name"

def test_raises_when_no_folder_exists():
    # Arrange
    repository = InMemoryFolderRepository()
    folder = Folder.create(name="folder")
    repository.save(folder=folder)
    use_case = RenameFolder(folder_repository=repository)

    # Act & Assert
    with pytest.raises(FolderNotFoundError):
        use_case.execute(folder_uuid=uuid4(), new_name="new_name")

def test_raises_when_new_name_already_exists():
    # Arrange
    repository = InMemoryFolderRepository()
    folder_to_rename = Folder.create(name="folder")
    other_folder = Folder.create(name="other_folder")
    repository.save(folder=folder_to_rename)
    repository.save(folder=other_folder)
    use_case = RenameFolder(folder_repository=repository)

    # Act & Assert
    with pytest.raises(DuplicateFolderNameError):
        use_case.execute(folder_uuid=folder_to_rename.id, new_name="other_folder")

def test_can_rename_folder_to_its_own_current_name():
    # Arrange
    repository = InMemoryFolderRepository()
    folder = Folder.create(name="folder")
    repository.save(folder=folder)
    use_case = RenameFolder(folder_repository=repository)

    # Act
    result = use_case.execute(folder_uuid=folder.id, new_name="folder")

    # Assert
    assert result.name == "folder"