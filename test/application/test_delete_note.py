from application.use_cases.note.CreateNote import CreateNote
from application.use_cases.note.DeleteNote import DeleteNote
from domain.INoteRepository import INoteRepository
from test.fakes.in_memory_note_repository import InMemoryNoteRepository


def test_delete_note_with_valid_uuid_succeeds() -> None:
    # Arrange
    repository: INoteRepository = InMemoryNoteRepository()

    use_case_create = CreateNote(note_repository=repository)
    note = use_case_create.execute(title="title", content="content")

    use_case_delete = DeleteNote(note_repository=repository)

    # Act
    use_case_delete.execute(note_uuid=note.id)

    # Assert
    assert repository.get_all() == []
