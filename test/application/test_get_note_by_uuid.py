from uuid import uuid4

from application.use_cases.note.GetNoteByUUID import GetNoteByUUID
from domain.Note import Note
from test.fakes.in_memory_note_repository import InMemoryNoteRepository


def test_get_note_by_uuid_succeeds():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")
    repository.save(note)
    use_case = GetNoteByUUID(repository)

    # Act & Assert
    assert note == use_case.execute(note.id)

def test_get_note_by_uuid_unknown_uuid():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")
    repository.save(note)
    use_case = GetNoteByUUID(repository)

    # Act
    note = use_case.execute(uuid4())

    # Assert
    assert note is None

def test_get_note_by_uuid_when_no_notes():
    # Arrange
    repository = InMemoryNoteRepository()
    use_case = GetNoteByUUID(repository)

    # Act
    note = use_case.execute(uuid4())

    # Assert
    assert note is None