class NoteNotFoundError(LookupError):
    """
    NoteNotFoundError is raised when a note with a given UUID
    cannot be found in repository
    """
    pass