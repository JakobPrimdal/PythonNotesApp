from uuid import UUID

from domain.errors.FolderNotFoundError import FolderNotFoundError
from domain.interfaces.IFolderRepository import IFolderRepository


class DeleteFolder:
    """
    Use case: To delete a folder - domain entity
    """
    def __init__(self, folder_repository: IFolderRepository) -> None:
        self._folder_repository = folder_repository

    def execute(self, folder_uuid: UUID) -> None:
        folder = self._folder_repository.get_by_uuid(folder_uuid)
        if folder is None:
            raise FolderNotFoundError(f"Folder with uuid {folder_uuid} not found")
        self._folder_repository.delete(folder_uuid)