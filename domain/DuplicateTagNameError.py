class DuplicateTagNameError(ValueError):
    """
    DuplicateTagNameError is raised when attempting to create
    or rename a tag to a name that is already used by another tag
    """
    pass