from uuid import uuid4

import pytest

from application.use_cases.note.AddTagToNote import AddTagToNote
from domain.Note import Note
from domain.Tag import Tag
from domain.errors.NoteNotFoundError import NoteNotFoundError
from domain.errors.TagNotFoundError import TagNotFoundError
from test.fakes.in_memory_tag_repository import InMemoryTagRepository
from test.fakes.in_memory_note_repository import InMemoryNoteRepository


def test_add_tag_to_note_succeeds():
    # Arrange
    note_repository = InMemoryNoteRepository()
    tag_repository = InMemoryTagRepository()
    note = Note.create(title="title", content="content")
    tag = Tag.create(name="tag")

    tag_repository.save(tag)
    note_repository.save(note)

    use_case = AddTagToNote(note_repository=note_repository, tag_repository=tag_repository)

    # Act
    result = use_case.execute(
        note_uuid=note.id,
        tag_uuid=tag.id
    )

    # Assert
    assert result.tag_ids == [tag.id]

    saved_note = note_repository.get_by_uuid(note.id)
    assert saved_note is not None
    assert saved_note.tag_ids == [tag.id]


def test_raises_when_note_does_not_exist():
    # Arrange
    note_repository = InMemoryNoteRepository()
    tag_repository = InMemoryTagRepository()

    tag = Tag.create(name="tag")
    tag_repository.save(tag)

    use_case = AddTagToNote(note_repository=note_repository, tag_repository=tag_repository)
    # Act & Assert
    with pytest.raises(NoteNotFoundError):
        use_case.execute(
            note_uuid=uuid4(),
            tag_uuid=tag.id
        )


def test_raises_when_note_is_archived():
    # Arrange
    note_repository = InMemoryNoteRepository()
    tag_repository = InMemoryTagRepository()
    note = Note.create(title="title", content="content")
    note.archive()
    note_repository.save(note)

    tag = Tag.create(name="tag")
    tag_repository.save(tag)

    use_case = AddTagToNote(note_repository=note_repository, tag_repository=tag_repository)

    # Act & Assert
    with pytest.raises(ValueError):
        use_case.execute(
            note_uuid=note.id,
            tag_uuid=tag.id
        )


def test_raises_when_tag_is_already_added():
    # Arrange
    note_repository = InMemoryNoteRepository()
    tag_repository = InMemoryTagRepository()
    note = Note.create(title="title", content="content")

    tag = Tag.create(name="tag")
    tag_repository.save(tag)

    note.add_tag(tag.id)
    note_repository.save(note)

    use_case = AddTagToNote(note_repository=note_repository, tag_repository=tag_repository)

    # Act & Assert
    with pytest.raises(ValueError):
        use_case.execute(
            note_uuid=note.id,
            tag_uuid=tag.id
        )

def test_raises_when_tag_does_not_exist():
    # Arrange
    note_repository = InMemoryNoteRepository()
    tag_repository = InMemoryTagRepository()
    note = Note.create(title="title", content="content")

    note_repository.save(note)

    use_case = AddTagToNote(note_repository=note_repository, tag_repository=tag_repository)

    # Act & Assert
    with pytest.raises(TagNotFoundError):
        use_case.execute(
            note_uuid=note.id,
            tag_uuid=uuid4()
        )