from uuid import uuid4

from application.use_cases.tag.DeleteTag import DeleteTag
from domain.Note import Note
from domain.Tag import Tag
from domain.interfaces.INoteRepository import INoteRepository
from domain.interfaces.ITagRepository import ITagRepository
from test.fakes.in_memory_note_repository import InMemoryNoteRepository
from test.fakes.in_memory_tag_repository import InMemoryTagRepository

import pytest


def test_discard_tag_removes_from_notes_including_archived_ones():
    # Arrange
    note_repository: INoteRepository = InMemoryNoteRepository()
    tag_repository: ITagRepository = InMemoryTagRepository()

    note = Note.create(title="title", content="content")
    note2 = Note.create(title="title2", content="content2")
    tag = Tag.create(name="tag")

    note.add_tag(tag.id)
    note2.add_tag(tag.id)
    note.archive()
    note2.archive()

    note_repository.save(note=note)
    note_repository.save(note=note2)
    tag_repository.save(tag)

    use_case_delete = DeleteTag(note_repository=note_repository, tag_repository=tag_repository)

    # Act
    use_case_delete.execute(tag.id)

    # Assert
    assert note.tag_ids == [] and note2.tag_ids == []

def test_discard_tag_reference_raises_when_tag_not_present():
    # Arrange
    note = Note.create(title="title", content="content")

    # Act & Arrange
    with pytest.raises(ValueError):
        note.discard_tag_reference(uuid4())
