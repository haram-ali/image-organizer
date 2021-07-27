from os import listdir, rename, makedirs

from os.path import isfile, isdir, dirname, splitext, exists
from os.path import basename as filename
from os.path import join as join_path
from os.path import exists as path_exists


from shutil import copyfile


"""
    Get files/Directories
"""


def getDirsInCurrDir(path):
    return [f for f in listdir(path) if isdir(join_path(path, f))]


def getFilesInCurrDir(path, extensions=None):
    allFiles = [f for f in listdir(path) if isfile(join_path(path, f))]

    if extensions:
        return [f for f in allFiles if getFileExtension(f) in extensions]
    return allFiles


"""
    Move/Copy files
"""


def moveFile(fromPath, toPath):
    try:
        if chkFile(toPath):
            raise FileExistsError

        mkDir(getFilePath(toPath))
        rename(fromPath, toPath)
    except FileExistsError:
        return FileExistsError
    except FileNotFoundError:
        return FileNotFoundError
    except:
        return Exception


def copyFile(fromPath, toPath):
    try:
        if chkFile(toPath):
            raise FileExistsError

        mkDir(getFilePath(toPath))
        copyfile(fromPath, toPath)
    except FileExistsError:
        return FileExistsError
    except FileNotFoundError:
        return FileNotFoundError
    except:
        return Exception


"""
    Get all files
"""


def getAllFiles(searchingDirPath, relativePath=False, extensions=None):
    """
    Returns all the files in current directory & all subdirectories.

    Parameters:
    ----------
    searchingDirPath (str):
        Full path to directory
    relativePath (Boolean): optional
        If true the files path will not include path to searching directory
    extensions: optional
        List of extensions to filter files.
    """

    def getAllFilesInner(path, extensions):
        files = []
        nonlocal searchingDirPath

        for dir in getDirsInCurrDir(path):
            files += getAllFilesInner(f'{path}/{dir}', extensions)

        currDirFiles = getFilesInCurrDir(path, extensions)
        files += putRelativePathToFiles(currDirFiles,
                                            path, searchingDirPath)
        return files

    files = getAllFilesInner(searchingDirPath, extensions)
    if relativePath:
        return files

    return putPathToFiles(files, searchingDirPath)


"""
    Utilities
"""


def writeToFile(file, content):
    with open(file, 'w') as file:
        file.write(content)


def chkFile(path):
    return exists(path)


def getFilePath(file):
    return dirname(file)


def getFileName(file):
    return filename(file)


def getFileExtension(file):
    return splitext(file)[1]


def mkDir(path):
    if not path_exists(path):
        makedirs(path)


def putPathToFiles(files, path):
    return [f'{path}/{f}' for f in files]


def putRelativePathToFiles(files, path, pathToDir):
    return [f'{path.replace(pathToDir, "")}/{file}' for file in files]
