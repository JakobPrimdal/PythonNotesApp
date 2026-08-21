from uuid import uuid4

import pytest

from application.use_cases.note.MarkNoteAsFavorite import MarkNoteAsFavorite
from domain.Note import Note
from domain.errors.NoteNotFoundError import NoteNotFoundError
from test.fakes.in_memory_note_repository import InMemoryNoteRepository


def test_mark_note_as_favorite_succeeds():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")
    repository.save(note)

    use_case = MarkNoteAsFavorite(note_repository=repository)

    # Act
    result = use_case.execute(note_uuid=note.id)

    # Assert
    assert result.is_favorite is True

    saved_note = repository.get_by_uuid(note.id)
    assert saved_note is not None
    assert saved_note.is_favorite is True


def test_raises_when_note_does_not_exist():
    # Arrange
    repository = InMemoryNoteRepository()
    use_case = MarkNoteAsFavorite(note_repository=repository)

    # Act & Assert
    with pytest.raises(NoteNotFoundError):
        use_case.execute(note_uuid=uuid4())


def test_raises_when_note_is_archived():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")
    note.archive()
    repository.save(note)

    use_case = MarkNoteAsFavorite(note_repository=repository)

    # Act & Assert
    with pytest.raises(ValueError):
        use_case.execute(note_uuid=note.id)


def test_raises_when_note_is_already_favorite():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")
    note.mark_as_favorite()
    repository.save(note)

    use_case = MarkNoteAsFavorite(note_repository=repository)

    # Act & Assert
    with pytest.raises(ValueError):
        use_case.execute(note_uuid=note.id)