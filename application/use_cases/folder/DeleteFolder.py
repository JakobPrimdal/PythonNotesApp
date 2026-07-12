from uuid import UUID

from domain.interfaces.IFolderRepository import IFolderRepository


class DeleteFolder:
    """
    Use case: To delete a folder - domain entity
    """
    def __init__(self, folder_repository: IFolderRepository) -> None:
        self._folder_repository = folder_repository

    def execute(self, folder_uuid: UUID) -> None:
        self._folder_repository.delete(folder_uuid)