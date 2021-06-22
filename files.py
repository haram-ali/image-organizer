from os import listdir, rename, makedirs

from os.path import isfile, isdir, dirname, splitext, exists
from os.path import basename as filename
from os.path import join as join_path
from os.path import exists as path_exists


from shutil import copyfile


"""
    Get files/Directories
"""


def get_dirs_in_curr_dir(path):
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
    try:
        if chk_file(from_path):
            raise FileExistsError

        mk_dir(get_file_path(to_path))
        rename(from_path, to_path)
    except FileExistsError:
        return FileExistsError
    except FileNotFoundError:
        return FileNotFoundError
    except:
        return Exception


def copy_file(from_path, to_path):
    try:
        if chk_file(from_path):
            raise FileExistsError

        mk_dir(get_file_path(to_path))
        copyfile(from_path, to_path)
    except FileExistsError:
        return FileExistsError
    except FileNotFoundError:
        return FileNotFoundError
    except:
        return Exception


"""
    Get all files
"""


def get_all_files(searching_dir_path, relative_path=False, extensions=None):
    """
    Returns all the files in current directory & all subdirectories.

    Parameters:
    ----------
    searching_dir_path (str):
        Full path to directory
    relative_path (Boolean): optional
        If true the files path will not include path to searching directory
    extensions: optional
        List of extensions to filter files.
    """

    def get_all_files_inner(path, extensions):
        files = []
        nonlocal searching_dir_path

        for dir in get_dirs_in_curr_dir(path):
            files += get_all_files_inner(f'{path}/{dir}', extensions)

        curr_dir_files = get_files_in_curr_dir(path, extensions)
        files += put_relative_path_to_files(curr_dir_files,
                                            path, searching_dir_path)
        return files

    files = get_all_files_inner(searching_dir_path, extensions)
    if relative_path:
        return files

    return put_path_to_files(files, searching_dir_path)


"""
    Utilities
"""


def write_to_file(file, content):
    with open(file, 'w') as file:
        file.write(content)


def chk_file(path):
    return exists(path)


def get_file_path(file):
    return dirname(file)


def get_file_name(file):
    return filename(file)


def get_file_extension(file):
    return splitext(file)[1]


def mk_dir(path):
    if not path_exists(path):
        makedirs(path)


def put_path_to_files(files, path):
    return [f'{path}/{f}' for f in files]


def put_relative_path_to_files(files, path, path_to_dir):
    return [f'{path.replace(path_to_dir, "")}/{file}' for file in files]
