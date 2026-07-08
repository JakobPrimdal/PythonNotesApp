import pytest

from application.CreateNote import CreateNote
from domain.Note import Note
from test.fakes.in_memory_note_repository import InMemoryNoteRepository


def test_create_note_saves_note_with_correct_data():
    # Arrange
    repository = InMemoryNoteRepository()
    use_case = CreateNote(note_repository=repository)

    # Act
    note = use_case.execute(title="title", content="content")

    # Assert
    saved_note = repository.get_by_uuid(note.id)
    assert saved_note is not None
    assert saved_note.title == "title"
    assert saved_note.content == "content"

def test_create_note_returns_the_created_note():
    # Arrange
    repository = InMemoryNoteRepository()
    use_case = CreateNote(note_repository=repository)

    # Act
    note = use_case.execute(title="title", content="content")

    # Assert
    assert isinstance(note, Note)
    assert note.title == "title"
    assert note.content == "content"

def test_create_note_with_invalid_data_raises_error_and_does_not_save():
    # Arrange
    repository = InMemoryNoteRepository()
    use_case = CreateNote(note_repository=repository)

    # Act & Assert
    with pytest.raises(ValueError):
        use_case.execute(title="", content="")

    assert repository.get_all() == []