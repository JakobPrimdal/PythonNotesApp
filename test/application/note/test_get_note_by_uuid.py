from uuid import uuid4

import pytest

from application.use_cases.note.GetNoteByUUID import GetNoteByUUID
from domain.Note import Note
from domain.errors.NoteNotFoundError import NoteNotFoundError
from test.fakes.in_memory_note_repository import InMemoryNoteRepository


def test_get_note_by_uuid_succeeds():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")
    repository.save(note)
    use_case = GetNoteByUUID(repository)

    # Act & Assert
    assert note == use_case.execute(note.id)

def test_raises_when_note_does_not_exist():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")
    repository.save(note)
    use_case = GetNoteByUUID(repository)

    # Act & Assert
    with pytest.raises(NoteNotFoundError):
        use_case.execute(uuid4())

def test_raises_when_no_notes_exist_at_all():
    # Arrange
    repository = InMemoryNoteRepository()
    use_case = GetNoteByUUID(repository)

    # Act & Assert
    with pytest.raises(NoteNotFoundError):
        use_case.execute(uuid4())