from typing import runtime_checkable, Protocol, Optional
from uuid import UUID

from domain.Folder import Folder


@runtime_checkable
class IFolderRepository(Protocol):
    def get_by_uuid(self, folder_uuid: UUID) -> Optional[Folder]:
        ...

    def get_all(self) -> list[Folder]:
        ...

    def save(self, folder: Folder) -> None:
        ...

    def delete(self, folder_uuid: UUID) -> None:
        ...