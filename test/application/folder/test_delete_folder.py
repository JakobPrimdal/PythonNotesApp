from uuid import uuid4

from application.use_cases.folder.DeleteFolder import DeleteFolder
from domain.Folder import Folder
from test.fakes.in_memory_folder_repository import InMemoryFolderRepository


def test_delete_folder_by_uuid_succeeds() -> None:
    # Arrange
    repository = InMemoryFolderRepository()
    folder = Folder.create("folder")
    repository.save(folder)
    use_case = DeleteFolder(repository)

    # Act
    use_case.execute(folder.id)

    # Assert
    assert repository.get_all() == []

def test_delete_folder_by_unknown_uuid_does_not_raise() -> None:
    # Arrange
    repository = InMemoryFolderRepository()
    folder = Folder.create("folder")
    repository.save(folder)
    use_case = DeleteFolder(repository)

    # Act
    use_case.execute(uuid4())

    # Assert
    assert repository.get_all() == [folder]