from application.use_cases.note.GetAllNotes import GetAllNotes
from domain.Note import Note
from test.fakes.in_memory_note_repository import InMemoryNoteRepository


def test_get_all_notes_succeeds():
    # Arrange
    repository = InMemoryNoteRepository()

    note1 = Note.create(title="title", content="content")
    note2 = Note.create(title="title2", content="content2")
    repository.save(note1)
    repository.save(note2)

    use_case = GetAllNotes(repository)

    # Act & Assert
    assert use_case.execute() == [note1, note2]


def test_get_all_notes_when_no_notes_succeeds():
    # Arrange
    repository = InMemoryNoteRepository()
    use_case = GetAllNotes(repository)

    # Act
    notes = use_case.execute()

    # & Assert
    assert notes == []