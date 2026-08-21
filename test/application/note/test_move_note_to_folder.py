from uuid import uuid4

import pytest

from application.use_cases.note.MoveNoteToFolder import MoveNoteToFolder
from domain.Folder import Folder
from domain.Note import Note
from domain.errors.FolderNotFoundError import FolderNotFoundError
from domain.errors.NoteNotFoundError import NoteNotFoundError
from test.fakes.in_memory_folder_repository import InMemoryFolderRepository
from test.fakes.in_memory_note_repository import InMemoryNoteRepository


def test_move_note_to_folder_succeeds():
    # Arrange
    note_repository = InMemoryNoteRepository()
    folder_repository = InMemoryFolderRepository()

    note = Note.create(title="title", content="content")
    folder = Folder.create(name="folder")

    note_repository.save(note)
    folder_repository.save(folder)

    use_case = MoveNoteToFolder(
        note_repository=note_repository,
        folder_repository=folder_repository
    )

    # Act
    result = use_case.execute(
        note_uuid=note.id,
        folder_uuid=folder.id
    )

    # Assert
    assert result.folder_id == folder.id

    saved_note = note_repository.get_by_uuid(note.id)
    assert saved_note is not None
    assert saved_note.folder_id == folder.id


def test_raises_when_note_does_not_exist():
    # Arrange
    note_repository = InMemoryNoteRepository()
    folder_repository = InMemoryFolderRepository()

    folder = Folder.create(name="folder")
    folder_repository.save(folder)

    use_case = MoveNoteToFolder(
        note_repository=note_repository,
        folder_repository=folder_repository
    )

    # Act & Assert
    with pytest.raises(NoteNotFoundError):
        use_case.execute(
            note_uuid=uuid4(),
            folder_uuid=folder.id
        )


def test_raises_when_folder_does_not_exist():
    # Arrange
    note_repository = InMemoryNoteRepository()
    folder_repository = InMemoryFolderRepository()

    note = Note.create(title="title", content="content")
    note_repository.save(note)

    use_case = MoveNoteToFolder(
        note_repository=note_repository,
        folder_repository=folder_repository
    )

    # Act & Assert
    with pytest.raises(FolderNotFoundError):
        use_case.execute(
            note_uuid=note.id,
            folder_uuid=uuid4()
        )


def test_raises_when_note_is_archived():
    # Arrange
    note_repository = InMemoryNoteRepository()
    folder_repository = InMemoryFolderRepository()

    note = Note.create(title="title", content="content")
    folder = Folder.create(name="folder")

    note.archive()

    note_repository.save(note)
    folder_repository.save(folder)

    use_case = MoveNoteToFolder(
        note_repository=note_repository,
        folder_repository=folder_repository
    )

    # Act & Assert
    with pytest.raises(ValueError):
        use_case.execute(
            note_uuid=note.id,
            folder_uuid=folder.id
        )


def test_note_is_not_moved_when_folder_does_not_exist():
    # Arrange
    note_repository = InMemoryNoteRepository()
    folder_repository = InMemoryFolderRepository()

    original_folder = Folder.create(name="original")
    note = Note.create(title="title", content="content")

    note.set_folder_id(original_folder.id)

    note_repository.save(note)
    folder_repository.save(original_folder)

    use_case = MoveNoteToFolder(
        note_repository=note_repository,
        folder_repository=folder_repository
    )

    # Act & Assert
    with pytest.raises(FolderNotFoundError):
        use_case.execute(
            note_uuid=note.id,
            folder_uuid=uuid4()
        )

    # Assert
    saved_note = note_repository.get_by_uuid(note.id)
    assert saved_note is not None
    assert saved_note.folder_id == original_folder.id