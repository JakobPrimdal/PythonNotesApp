from uuid import UUID

from domain.interfaces.INoteRepository import INoteRepository
from domain.interfaces.IFolderRepository import IFolderRepository
from domain.Note import Note
from domain.errors.NoteNotFoundError import NoteNotFoundError
from domain.errors.FolderNotFoundError import FolderNotFoundError


class MoveNoteToFolder:
    def __init__(
        self,
        note_repository: INoteRepository,
        folder_repository: IFolderRepository
    ) -> None:
        self._note_repository = note_repository
        self._folder_repository = folder_repository

    def execute(self, note_uuid: UUID, folder_uuid: UUID) -> Note:
        note = self._note_repository.get_by_uuid(note_uuid)
        if note is None:
            raise NoteNotFoundError(f"Note with uuid {note_uuid} not found")

        folder = self._folder_repository.get_by_uuid(folder_uuid)
        if folder is None:
            raise FolderNotFoundError(f"Folder with uuid {folder_uuid} not found")

        note.set_folder_id(folder_uuid)
        self._note_repository.save(note)
        return note