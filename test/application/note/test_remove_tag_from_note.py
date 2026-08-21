from uuid import uuid4

import pytest

from application.use_cases.note.RemoveTagFromNote import RemoveTagFromNote
from domain.Note import Note
from domain.errors.NoteNotFoundError import NoteNotFoundError
from test.fakes.in_memory_note_repository import InMemoryNoteRepository


def test_remove_tag_from_note_succeeds():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")
    tag_uuid = uuid4()

    note.add_tag(tag_uuid)
    repository.save(note)

    use_case = RemoveTagFromNote(note_repository=repository)

    # Act
    result = use_case.execute(
        note_uuid=note.id,
        tag_uuid=tag_uuid
    )

    # Assert
    assert result.tag_ids == []

    saved_note = repository.get_by_uuid(note.id)
    assert saved_note is not None
    assert saved_note.tag_ids == []


def test_raises_when_note_does_not_exist():
    # Arrange
    repository = InMemoryNoteRepository()
    use_case = RemoveTagFromNote(note_repository=repository)

    # Act & Assert
    with pytest.raises(NoteNotFoundError):
        use_case.execute(
            note_uuid=uuid4(),
            tag_uuid=uuid4()
        )


def test_raises_when_note_is_archived():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")
    tag_uuid = uuid4()

    note.add_tag(tag_uuid)
    note.archive()

    repository.save(note)

    use_case = RemoveTagFromNote(note_repository=repository)

    # Act & Assert
    with pytest.raises(ValueError):
        use_case.execute(
            note_uuid=note.id,
            tag_uuid=tag_uuid
        )


def test_raises_when_tag_does_not_exist_on_note():
    # Arrange
    repository = InMemoryNoteRepository()
    note = Note.create(title="title", content="content")
    repository.save(note)

    use_case = RemoveTagFromNote(note_repository=repository)

    # Act & Assert
    with pytest.raises(ValueError):
        use_case.execute(
            note_uuid=note.id,
            tag_uuid=uuid4()
        )