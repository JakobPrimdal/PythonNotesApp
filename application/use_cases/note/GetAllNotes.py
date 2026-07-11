from domain.INoteRepository import INoteRepository
from domain.Note import Note


class GetAllNotes:
    """
    Use case: To retrieve all notes from DB
    """

    def __init__(self, note_repository: INoteRepository) -> None:
        self._note_repository = note_repository

    def execute(self) -> list[Note]:
        notes = self._note_repository.get_all()
        return notes