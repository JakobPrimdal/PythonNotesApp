from uuid import uuid4

from application.use_cases.folder.GetFolderByUUID import GetFolderByUUID
from domain.Folder import Folder
from test.fakes.in_memory_folder_repository import InMemoryFolderRepository


def test_get_folder_by_uuid_succeeds():
    # Arrange
    repository = InMemoryFolderRepository()
    folder = Folder.create(name="folder")
    repository.save(folder)
    use_case = GetFolderByUUID(repository)

    # Act & Assert
    assert folder == use_case.execute(folder.id)

def test_get_folder_by_unknown_uuid():
    # Arrange
    repository = InMemoryFolderRepository()
    folder = Folder.create(name="folder")
    repository.save(folder)
    use_case = GetFolderByUUID(repository)

    # Act
    folder2 = use_case.execute(uuid4())

    # Assert
    assert folder2 is None

def test_get_note_by_uuid_when_no_notes():
    # Arrange
    repository = InMemoryFolderRepository()
    use_case = GetFolderByUUID(repository)

    # Act
    folder = use_case.execute(uuid4())

    # Assert
    assert folder is None