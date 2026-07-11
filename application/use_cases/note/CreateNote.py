from domain.interfaces.INoteRepository import INoteRepository
from domain.Note import Note


class CreateNote:
    """
    Use case: Create a new note

    Orchestras domain entity - Note - and persistence - INoteRepository,
    but does not hold any business logic or rules
    """

    def __init__(self, note_repository: INoteRepository) -> None:
        self._note_repository = note_repository

    def execute(self, title: str, content: str) -> Note:
        note = Note.create(title=title, content=content)
        self._note_repository.save(note)
        return note