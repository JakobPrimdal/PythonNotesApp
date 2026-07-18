from uuid import UUID

from domain.Folder import Folder
from domain.errors.DuplicateFolderNameError import DuplicateFolderNameError
from domain.errors.FolderNotFoundError import FolderNotFoundError
from domain.interfaces.IFolderRepository import IFolderRepository


class UpdateFolder:
    def __init__(self, folder_repository: IFolderRepository):
        self._folder_repository = folder_repository

    def execute(self, folder_uuid: UUID, new_name: str) -> Folder:
        folder = self._folder_repository.get_by_uuid(folder_uuid)
        if folder is None:
            raise FolderNotFoundError(f"Folder with uuid {folder_uuid} not found")

        other_folders = [f for f in self._folder_repository.get_all() if f.id != folder_uuid]
        if any(f.name == new_name for f in other_folders):
            raise DuplicateFolderNameError(f"Folder with name {new_name} already exists")

        folder.rename(new_name)
        self._folder_repository.save(folder)
        return folder