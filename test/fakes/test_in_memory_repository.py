from uuid import uuid4

from domain.Note import Note
from fakes.in_memory_note_repository import InMemoryNoteRepository


def test_save_and_get_by_id_returns_saved_note():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="Indkøb", content="Mælk")

    # Act
    repository.save(note)
    found_note = repository.get_by_uuid(note.id)

    # Assert
    assert found_note is note


def test_get_by_id_with_unknown_id_returns_none():
    # Arrange
    repository = InMemoryNoteRepository()

    # Act
    found_note = repository.get_by_uuid(uuid4())

    # Assert
    assert found_note is None


def test_get_all_returns_all_saved_notes():
    # Arrange
    repository = InMemoryNoteRepository()
    note_a = Note.create(title="Note A", content="")
    note_b = Note.create(title="Note B", content="")

    # Act
    repository.save(note_a)
    repository.save(note_b)

    # Assert
    result_ids = {note.id for note in repository.get_all()}
    assert result_ids == {note_a.id, note_b.id}


def test_delete_removes_note():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="Note", content="")
    repository.save(note)

    # Act
    repository.delete(note.id)

    # Assert
    assert repository.get_by_uuid(note.id) is None


def test_delete_unknown_id_does_not_raise_error():
    # Arrange
    repository = InMemoryNoteRepository()

    # Act & Assert (unknown uuid should not throw any exceptions)
    repository.delete(uuid4())