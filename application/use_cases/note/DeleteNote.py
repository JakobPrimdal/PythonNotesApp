from uuid import UUID

from domain.INoteRepository import INoteRepository


class DeleteNote:
    def __init__(self, note_repository: INoteRepository) -> None:
        self._note_repository = note_repository

    def execute(self, note_uuid: UUID) -> None:
        self._note_repository.delete(note_uuid)