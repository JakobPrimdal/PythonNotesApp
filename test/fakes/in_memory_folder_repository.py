from typing import Optional
from uuid import UUID

from domain.Folder import Folder


class InMemoryFolderRepository:
    """
    InMemoryFolderRepository is a simple implementation of IFolderRepository.

    Used only in tests, to test the application-layer's use cases without a real DB.
    Acts as a real repository (data is there, and query works - however, only in memory)
    """

    def __init__(self) -> None:
        self._folders: dict[UUID, Folder] = {}

    def get_by_uuid(self, folder_uuid: UUID) -> Optional[Folder]:
        return self._folders.get(folder_uuid)

    def get_all(self) -> list[Folder]:
        return list(self._folders.values())

    def save(self, folder: Folder) -> None:
        self._folders[folder.id] = folder

    def delete(self, folder_uuid: UUID) -> None:
        if folder_uuid in self._folders:
            del self._folders[folder_uuid]
