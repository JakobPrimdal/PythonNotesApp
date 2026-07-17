from application.use_cases.folder.GetAllFolders import GetAllFolders
from domain.Folder import Folder
from test.fakes.in_memory_folder_repository import InMemoryFolderRepository


def test_get_all_notes_succeeds():
    # Arrange
    repository = InMemoryFolderRepository()

    folder1 = Folder.create(name="folder1")
    folder2 = Folder.create(name="folder2")
    repository.save(folder1)
    repository.save(folder2)

    use_case = GetAllFolders(repository)

    # Act & Assert
    assert use_case.execute() == [folder1, folder2]


def test_get_all_notes_when_no_notes_succeeds():
    # Arrange
    repository = InMemoryFolderRepository()
    use_case = GetAllFolders(repository)

    # Act
    notes = use_case.execute()

    # & Assert
    assert notes == []