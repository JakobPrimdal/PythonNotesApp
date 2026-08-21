from uuid import uuid4

from application.use_cases.note.GetNotesByFolder import GetNotesByFolder
from domain.Folder import Folder
from domain.Note import Note
from test.fakes.in_memory_note_repository import InMemoryNoteRepository


def test_get_notes_by_folder_succeeds():
    # Arrange
    repository = InMemoryNoteRepository()

    folder = Folder.create(name="folder")

    note1 = Note.create(title="title1", content="content1")
    note2 = Note.create(title="title2", content="content2")

    note1.set_folder_id(folder.id)
    note2.set_folder_id(folder.id)

    repository.save(note1)
    repository.save(note2)

    use_case = GetNotesByFolder(note_repository=repository)

    # Act
    notes = use_case.execute(folder_uuid=folder.id)

    # Assert
    assert notes == [note1, note2]


def test_get_notes_by_folder_when_no_notes_exist_succeeds():
    # Arrange
    repository = InMemoryNoteRepository()
    use_case = GetNotesByFolder(note_repository=repository)

    folder_uuid = uuid4()

    # Act
    notes = use_case.execute(folder_uuid=folder_uuid)

    # Assert
    assert notes == []


def test_get_notes_by_folder_only_returns_notes_from_requested_folder():
    # Arrange
    repository = InMemoryNoteRepository()

    folder1 = Folder.create(name="folder1")
    folder2 = Folder.create(name="folder2")

    note1 = Note.create(title="title1", content="content1")
    note2 = Note.create(title="title2", content="content2")
    note3 = Note.create(title="title3", content="content3")

    note1.set_folder_id(folder1.id)
    note2.set_folder_id(folder1.id)
    note3.set_folder_id(folder2.id)

    repository.save(note1)
    repository.save(note2)
    repository.save(note3)

    use_case = GetNotesByFolder(note_repository=repository)

    # Act
    notes = use_case.execute(folder_uuid=folder1.id)

    # Assert
    assert notes == [note1, note2]
    assert note3 not in notes


def test_get_notes_by_folder_does_not_return_notes_without_a_folder():
    # Arrange
    repository = InMemoryNoteRepository()

    folder = Folder.create(name="folder")

    note_with_folder = Note.create(
        title="folder note",
        content="content"
    )

    note_without_folder = Note.create(
        title="unfiled note",
        content="content"
    )

    note_with_folder.set_folder_id(folder.id)

    repository.save(note_with_folder)
    repository.save(note_without_folder)

    use_case = GetNotesByFolder(note_repository=repository)

    # Act
    notes = use_case.execute(folder_uuid=folder.id)

    # Assert
    assert notes == [note_with_folder]
    assert note_without_folder not in notes