from uuid import uuid4

import pytest

from application.use_cases.note.UnarchiveNote import UnarchiveNote
from domain.Note import Note
from domain.errors.NoteNotFoundError import NoteNotFoundError
from test.fakes.in_memory_note_repository import InMemoryNoteRepository


def test_unarchive_note_succeeds():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")
    note.archive()
    repository.save(note)

    use_case = UnarchiveNote(note_repository=repository)

    # Act
    result = use_case.execute(note_uuid=note.id)

    # Assert
    assert result.is_archived is False

    saved_note = repository.get_by_uuid(note.id)
    assert saved_note is not None
    assert saved_note.is_archived is False


def test_raises_when_note_does_not_exist():
    # Arrange
    repository = InMemoryNoteRepository()
    use_case = UnarchiveNote(note_repository=repository)

    # Act & Assert
    with pytest.raises(NoteNotFoundError):
        use_case.execute(note_uuid=uuid4())


def test_raises_when_note_is_not_archived():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")
    repository.save(note)

    use_case = UnarchiveNote(note_repository=repository)

    # Act & Assert
    with pytest.raises(ValueError):
        use_case.execute(note_uuid=note.id)