# test/application/test_create_folder.py
import pytest

from application.use_cases.folder.CreateFolder import CreateFolder
from domain.errors.DuplicateFolderNameError import DuplicateFolderNameError
from test.fakes.in_memory_folder_repository import InMemoryFolderRepository


def test_create_persists_folder():
    # Arrange
    repository = InMemoryFolderRepository()
    use_case = CreateFolder(folder_repository=repository)

    # Act
    result = use_case.execute("Work")

    # Assert
    assert result.name == "Work"
    persisted_folder = repository.get_by_uuid(result.id)
    assert persisted_folder is not None
    assert persisted_folder.name == "Work"


def test_raises_when_name_already_exists():
    # Arrange
    repository = InMemoryFolderRepository()
    use_case = CreateFolder(folder_repository=repository)
    use_case.execute("Work")

    # Act & Assert
    with pytest.raises(DuplicateFolderNameError):
        use_case.execute("Work")


def test_does_not_save_when_name_is_invalid():
    # Arrange
    repository = InMemoryFolderRepository()
    use_case = CreateFolder(folder_repository=repository)

    # Act & Assert
    with pytest.raises(ValueError):
        use_case.execute("")

    assert repository.get_all() == []