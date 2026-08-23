from uuid import uuid4

import pytest

from application.use_cases.folder.GetFolderByUUID import GetFolderByUUID
from domain.Folder import Folder
from domain.errors.FolderNotFoundError import FolderNotFoundError
from test.fakes.in_memory_folder_repository import InMemoryFolderRepository


def test_get_folder_by_uuid_succeeds():
    # Arrange
    repository = InMemoryFolderRepository()
    folder = Folder.create(name="folder")
    repository.save(folder)
    use_case = GetFolderByUUID(repository)

    # Act & Assert
    assert folder == use_case.execute(folder.id)

def test_raises_when_folder_does_not_exist():
    # Arrange
    repository = InMemoryFolderRepository()
    folder = Folder.create(name="folder")
    repository.save(folder)
    use_case = GetFolderByUUID(repository)

    # Act & Assert
    with pytest.raises(FolderNotFoundError):
        use_case.execute(uuid4())

def test_raises_when_no_folders_exist_at_all():
    # Arrange
    repository = InMemoryFolderRepository()
    use_case = GetFolderByUUID(repository)

    # Act & Assert
    with pytest.raises(FolderNotFoundError):
        use_case.execute(uuid4())