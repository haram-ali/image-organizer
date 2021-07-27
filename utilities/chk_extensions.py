from private_constants import INPUT_DIR
from files import getAllFiles, getFileExtension


def chkExtensions():
    files = getAllFiles(INPUT_DIR)
    extensions = [getFileExtension(file) for file in files]

    # Removing duplicats
    extensions = list(dict.fromkeys(extensions))

    print(*extensions, sep='\n')
