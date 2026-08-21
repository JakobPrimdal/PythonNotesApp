from uuid import uuid4

import pytest

from application.use_cases.note.UpdateNoteContent import UpdateNoteContent
from domain.errors.NoteNotFoundError import NoteNotFoundError
from domain.Note import Note
from test.fakes.in_memory_note_repository import InMemoryNoteRepository


def test_update_note_content_persists():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")
    repository.save(note)
    use_case = UpdateNoteContent(note_repository=repository)

    # Act
    result = use_case.execute(note.id, "new_content")

    # Assert
    assert result.content == "new_content"

    saved_note = repository.get_by_uuid(note.id)
    assert saved_note is not None
    assert saved_note.content == "new_content"


def test_raises_when_note_does_not_exist():
    # Arrange
    repository = InMemoryNoteRepository()
    use_case = UpdateNoteContent(note_repository=repository)

    # Act & Assert
    with pytest.raises(NoteNotFoundError):
        use_case.execute(note_uuid=uuid4(), new_content="new_content")


def test_raises_when_note_is_archived():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")
    note.archive()
    repository.save(note)

    use_case = UpdateNoteContent(note_repository=repository)

    # Act & Assert
    with pytest.raises(ValueError):
        use_case.execute(note_uuid=note.id, new_content="new_content")


def test_raises_when_new_content_would_make_note_empty():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")

    note.update_title("")

    repository.save(note)

    use_case = UpdateNoteContent(note_repository=repository)

    # Act & Assert
    with pytest.raises(ValueError):
        use_case.execute(
            note_uuid=note.id,
            new_content=""
        )