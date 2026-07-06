import uuid

import pytest

from domain.Note import Note


def test_create_note_with_title_and_content_succeeds():
    # Arrange & Act
    note = Note.create(title="title", content="content")

    # Assert
    assert note.title == "title"
    assert note.content == "content"
    assert note.created_at is not None
    assert note.is_archived == False
    assert note.is_favorite == False
    assert note.folder_id is None
    assert note.tags == []

def test_create_create_note_with_only_title_sucseeds():
    # Arrange & Act
    note = Note.create(title="title", content="")

    # Assert
    assert note.title == "title"
    assert note.content == ""

def test_create_create_note_with_only_content_succeeds():
    # Arrange & Act
    note = Note.create(title="", content="content")

    # Assert
    assert note.title == ""
    assert note.content == "content"

def test_create_note_with_empty_title_and_content_raises_error():
    # Act & Assert
    with pytest.raises(ValueError):
        Note.create(title="", content="")

def test_create_note_with_only_whitespace_raises_error():
    # Act & Arrange
    with pytest.raises(ValueError):
        Note.create(title=" ", content=" ")

def test_update_title_changes_title():
    # Arrange
    note = Note.create(title="title", content="content")

    # Act
    note.update_title("new_title")

    # Assert
    assert note.title == "new_title"

def test_update_content_changes_content():
    # Arrange
    note = Note.create(title="title", content="content")

    # Act
    note.update_content("new_content")

    # Assert
    assert note.content == "new_content"

def test_update_title_to_empty_when_content_also_empty_raises_error():
    # Arrange
    note = Note.create(title="title", content="")

    # Act & Assert
    with pytest.raises(ValueError):
        note.update_title("")

def test_update_content_to_empty_when_title_also_empty_raises_error():
    # Arrange
    note = Note.create(title="", content="content")

    # Act & Assert
    with pytest.raises(ValueError):
        note.update_content("")

def test_archive_note_sets_is_archived_succeeds():
    # Arrange
    note = Note.create(title="title", content="content")

    # Act
    note.archive()

    # Assert
    assert note.is_archived == True

def test_unarchive_note_sets_is_unarchived():
    # Arrange
    note = Note.create(title="title", content="content")
    note.archive()

    # Act
    note.unarchive()

    # Assert
    assert note.is_archived == False

def test_archiving_already_archived_note_raises_error():
    # Arrange
    note = Note.create(title="title", content="content")
    note.archive()

    # Act & Assert
    with pytest.raises(ValueError):
        note.archive()

def test_unarchiving_non_archived_note_raises_error():
    # Arrange
    note = Note.create(title="title", content="content")

    # Act & Arrange
    with pytest.raises(ValueError):
        note.unarchive()

def test_cannot_update_title_on_archived_note():
    # Arrange
    note = Note.create(title="title", content="content")
    note.archive()

    # Act & Assert
    with pytest.raises(ValueError):
        note.update_title("new_title")

def test_add_tag_adds_cleaned_tag():
    # Arrange
    note = Note.create(title="title", content="content")

    # Act
    note.add_tag("   new_tag   ")

    # Assert
    assert note.tags == ["new_tag"]

def test_add_duplicate_tag_raises_error():
    # Arrange
    note = Note.create(title="title", content="content")
    note.add_tag("tag")

    # Act & Assert
    with pytest.raises(ValueError):
        note.add_tag("tag")

def test_remove_tag_succeeds():
    # Arrange
    note = Note.create(title="title", content="content")
    note.add_tag("tag")

    # Act
    note.remove_tag("tag")

    # Assert
    assert note.tags == []

def test_remove_not_found_tag_raises_error():
    # Arrange
    note = Note.create(title="title", content="content")

    # Act & Assert
    with pytest.raises(ValueError):
        note.remove_tag("tag")

def test_remove_tag_on_archived_note_raises_error():
    # Arrange
    note = Note.create(title="title", content="content")
    note.add_tag("tag")
    note.archive()

    # Act & Assert
    with pytest.raises(ValueError):
        note.remove_tag("tag")

def test_mark_as_favorite_succeeds():
    # Arrange
    note = Note.create(title="title", content="content")

    # Act
    note.mark_as_favorite()

    # Assert
    assert note.is_favorite is True

def test_unmarked_favorite_note_succeeds():
    # Arrange
    note = Note.create(title="title", content="content")
    note.mark_as_favorite()

    # Act
    note.unmark_as_favorite()

    # Assert
    assert note.is_favorite is False

def test_cannot_mark_archived_note_as_favorite():
    # Arrange
    note = Note.create(title="title", content="content")
    note.archive()

    # Act & Assert
    with pytest.raises(ValueError):
        note.mark_as_favorite()

def test_cannot_unmark_archived_note_as_favorite():
    # Arrange
    note = Note.create(title="title", content="content")
    note.mark_as_favorite()
    note.archive()

    # Act & Assert
    with pytest.raises(ValueError):
        note.unmark_as_favorite()

def test_set_folder_id_sets_folder_id_succeeds():
    # Arrange
    note = Note.create(title="title", content="content")
    id = uuid.uuid4()

    # Act
    note.set_folder_id(folder_id=id)

    # Assert
    assert note.folder_id == id

def test_set_folder_id_on_archived_note_raises_error():
    # Arrange
    note = Note.create(title="title", content="content")
    note.archive()

    # Act & Assert
    with pytest.raises(ValueError):
        note.set_folder_id(folder_id=uuid.uuid4())