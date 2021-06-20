from os import listdir, rename, makedirs
from os.path import isfile, isdir, basename as filename, dirname, splitext, join as join_path, exists as dir_exists

from shutil import copyfile


"""
    File/Directories
"""


def get_all_files(path, extensions=None):
    """
    Returns all the files in current directory & all subdirectories.

    Parameters:
    ----------
    path (str):
        Full path to directory
    extensions: optional
        List of extensions to filter files.
    """

    def get_all_files_inner(path, extensions):
        files = []

        for dir in get_dirs(path):
            files += get_all_files_inner(f'{path}/{dir}', extensions)

        files += put_path_to_files(get_files_in_curr_dir(path,
                                   extensions), path)
        return files

    return get_all_files_inner(path, extensions)


"""
    Get files/Directories
"""

def get_dirs(path):
    return [f for f in listdir(path) if isdir(join_path(path, f))]


def get_files_in_curr_dir(path, extensions):
    all_files = [f for f in listdir(path) if isfile(join_path(path, f))]

    if extensions:
        return [f for f in all_files if get_file_extension(f) in extensions]
    return all_files


"""
    Move/Copy files
"""


def move_file(from_path, to_path):
    # TODO: What if file moving failed
    mk_dir(get_file_path(to_path))
    rename(from_path, to_path)

def copy_file(form_path, to_path):
    # TODO: What if file moving failed
    copyfile(form_path, to_path)


"""
    Utilities
"""


def get_file_extension(file):
    return splitext(file)[1]


def get_file_name(file):
    return filename(file)


def get_file_path(file):
    return dirname(file)

def mk_dir(path):
    if not dir_exists(path):
        makedirs(path)

def put_path_to_files(files, path):
    return [f'{path}/{f}' for f in files]
