from typing import Optional
from uuid import UUID

from domain.Folder import Folder
from domain.interfaces.IFolderRepository import IFolderRepository


class GetFolderByUUID:
    """
    Use case: used to retrieve a specific folder
    """

    def __init__(self, folder_repository: IFolderRepository) -> None:
        self._folder_repository = folder_repository

    def execute(self, folder_uuid: UUID) -> Optional[Folder]:
        folder = self._folder_repository.get_by_uuid(folder_uuid)
        return folder