from domain.Note import Note
from domain.interfaces.IFolderRepository import IFolderRepository


class GetAllFolders:
    """
    Use case: To retrieve all folders
    """
    def __init__(self, folder_repository: IFolderRepository) -> None:
        self._folder_repository = folder_repository

    def execute(self) -> list[Note]:
        notes = self._folder_repository.get_all()
        return notes