from uuid import uuid4

import pytest

from application.UpdateNoteTitle import UpdateNoteTitle
from domain.Note import Note
from domain.NoteNotFoundError import NoteNotFoundError
from test.fakes.in_memory_note_repository import InMemoryNoteRepository


def test_update_note_title_persists():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")
    repository.save(note)
    use_case = UpdateNoteTitle(note_repository=repository)

    # Act
    result = use_case.execute(note.id, "new_title")

    # Assert
    assert result.title == "new_title"

def test_raises_when_note_does_not_exist():
    # Arrange
    repository = InMemoryNoteRepository()
    use_case = UpdateNoteTitle(repository)

    # Act & Assert
    with pytest.raises(NoteNotFoundError):
        use_case.execute(note_uuid=uuid4(), new_title="new_title")


def test_raises_when_note_is_archived():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")
    note.archive()
    repository.save(note)

    use_case = UpdateNoteTitle(repository)

    # Act & Assert
    with pytest.raises(ValueError):
        use_case.execute(note_uuid=note.id, new_title="new_title")