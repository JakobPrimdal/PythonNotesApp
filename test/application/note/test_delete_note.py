import uuid
from uuid import uuid4

import pytest

from application.use_cases.note.DeleteNote import DeleteNote
from domain.Note import Note
from domain.errors.NoteNotFoundError import NoteNotFoundError
from domain.interfaces.INoteRepository import INoteRepository
from test.fakes.in_memory_note_repository import InMemoryNoteRepository


def test_delete_note_with_valid_uuid_succeeds() -> None:
    # Arrange
    repository: INoteRepository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")
    repository.save(note)
    use_case_delete = DeleteNote(note_repository=repository)

    # Act
    use_case_delete.execute(note_uuid=note.id)

    # Assert
    assert repository.get_all() == []

def test_delete_note_with_unknow_uuid_raises() -> None:
    # Arrange
    repository: INoteRepository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")
    repository.save(note)
    use_case = DeleteNote(note_repository=repository)

    # Act
    with pytest.raises(NoteNotFoundError):
        use_case.execute(note_uuid=uuid4())