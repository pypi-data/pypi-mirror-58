"""
    This file deal with file operations.
"""


def exists(path: str):
    """return if a given path is a file."""
    import os.path
    return os.path.isfile(path=path)


def file_and_extension(path: str):
    """return filename and their extension."""
    filename = path.split('/')[-1].split('.')[:-1][0]
    extension = path.split('.')[-1][0]
    return filename, extension
