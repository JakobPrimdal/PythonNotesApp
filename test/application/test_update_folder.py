from uuid import uuid4

import pytest

from application.use_cases.folder.UpdateFolder import UpdateFolder
from domain.Folder import Folder
from domain.errors.FolderNotFoundError import FolderNotFoundError
from test.fakes.in_memory_folder_repository import InMemoryFolderRepository


def test_update_folder_succeeds():
    # Arrange
    repository = InMemoryFolderRepository()
    folder = Folder.create(name="folder")
    repository.save(folder=folder)
    use_case = UpdateFolder(folder_repository=repository)

    # Act
    result = use_case.execute(folder_uuid=folder.id, new_name="new_name")

    # Assert
    assert result.name == "new_name"

def test_raises_when_no_folder_exists():
    # Arrange
    repository = InMemoryFolderRepository()
    folder = Folder.create(name="folder")
    repository.save(folder=folder)
    use_case = UpdateFolder(folder_repository=repository)

    # Act & Assert
    with pytest.raises(FolderNotFoundError):
        use_case.execute(folder_uuid=uuid4(), new_name="new_name")