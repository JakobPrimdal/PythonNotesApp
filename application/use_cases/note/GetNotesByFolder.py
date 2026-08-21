from uuid import UUID

from domain.interfaces.INoteRepository import INoteRepository
from domain.Note import Note


class GetNotesByFolder:
    def __init__(self, note_repository: INoteRepository) -> None:
        self._note_repository = note_repository

    def execute(self, folder_uuid: UUID) -> list[Note]:
        return self._note_repository.get_by_folder_id(folder_uuid)