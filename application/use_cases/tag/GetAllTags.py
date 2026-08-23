from domain.interfaces.ITagRepository import ITagRepository


class GetAllTags:
    """
    Use case: To retrieve all tags from DB
    """

    def __init__(self, tag_repository: ITagRepository):
        self._tag_repository = tag_repository

    def execute(self):
        return self._tag_repository.get_all()
