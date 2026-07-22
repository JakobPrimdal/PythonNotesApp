from uuid import UUID

from domain.errors.FolderNotFoundError import FolderNotFoundError
from domain.interfaces.IFolderRepository import IFolderRepository
from domain.interfaces.INoteRepository import INoteRepository


class DeleteFolder:
    """
    Use case: To delete a folder - domain entity
    """
    def __init__(self, folder_repository: IFolderRepository, note_repository: INoteRepository) -> None:
        self._folder_repository = folder_repository
        self._note_repository = note_repository

    def execute(self, folder_uuid: UUID) -> None:
        folder = self._folder_repository.get_by_uuid(folder_uuid)
        if folder is None:
            raise FolderNotFoundError(f"Folder with uuid {folder_uuid} not found")

        notes_in_folder = self._note_repository.get_by_folder_id(folder_uuid)
        for note in notes_in_folder:
            if note.is_archived:
                # Archived notes are lock and can't be changed
                # Archived notes keep their folder_id - even though
                # they now point to a non-existing folder
                continue
            note.set_folder_id(None)
            self._note_repository.save(note)

        self._folder_repository.delete(folder_uuid)