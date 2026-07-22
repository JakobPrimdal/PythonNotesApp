from uuid import uuid4

import pytest

from application.use_cases.folder.DeleteFolder import DeleteFolder
from domain.Folder import Folder
from domain.errors.FolderNotFoundError import FolderNotFoundError
from test.fakes.in_memory_note_repository import InMemoryNoteRepository
from test.fakes.in_memory_folder_repository import InMemoryFolderRepository


def test_delete_folder_by_uuid_succeeds() -> None:
    # Arrange
    folder_repository = InMemoryFolderRepository()
    note_repository = InMemoryNoteRepository()
    folder = Folder.create("folder")
    folder_repository.save(folder)
    use_case = DeleteFolder(folder_repository, note_repository)

    # Act
    use_case.execute(folder.id)

    # Assert
    assert folder_repository.get_all() == []

def test_delete_folder_by_unknown_uuid_raises() -> None:
    # Arrange
    folder_repository = InMemoryFolderRepository()
    note_repository = InMemoryNoteRepository()
    folder = Folder.create("folder")
    folder_repository.save(folder)
    use_case = DeleteFolder(folder_repository, note_repository)

    # Act
    with pytest.raises(FolderNotFoundError):
        use_case.execute(folder_uuid=uuid4())