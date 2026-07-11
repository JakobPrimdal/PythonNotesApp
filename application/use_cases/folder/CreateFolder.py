from domain.errors.DuplicateFolderNameError import DuplicateFolderNameError
from domain.Folder import Folder
from domain.interfaces.IFolderRepository import IFolderRepository


class CreateFolder:
    """
    Use case: Create a new folder

    Orchestras domain entity - Folder - add persistence - IFolderRepository,
    but does not hold any business logic or rules
    """

    def __init__(self, folder_repository: IFolderRepository):
        self._folder_repository = folder_repository

    def execute(self, name: str) -> Folder:
        if any (folder.name == name for folder in self._folder_repository.get_all()):
            raise DuplicateFolderNameError(f"Folder with name {name} already exists")
        folder = Folder.create(name=name)
        self._folder_repository.save(folder)
        return folder