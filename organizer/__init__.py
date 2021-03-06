from private_constants import INPUT_DIR, OUT_DIR
from files import getAllFiles
from .organize import organizeFiles
from stats import showStats


ALLOWED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.mp4']
COPY_FILES = True                   # If false then files will be move
USE_FILE_NAME_TO_ORGANIZE = True    # If false then OS attributes will be used
KEEP_SUB_DIR_SUTRUCTURE_INSIDE_DATE_DIRS = True     # If true then the dir structure will be preserved as in input dir


def organize():
    # Getting files
    files = getAllFiles(
        INPUT_DIR,
        relativePath=True,
        extensions=ALLOWED_EXTENSIONS
    )
    print(f'{len(files)} files found.')

    # Organizing files
    filesStatus = organizeFiles(
        files,
        INPUT_DIR,
        OUT_DIR,
        copyFiles=COPY_FILES,
        useFileNameToOrganize=USE_FILE_NAME_TO_ORGANIZE,
        keepSubDirSutructureInsideDateDirs=KEEP_SUB_DIR_SUTRUCTURE_INSIDE_DATE_DIRS
    )

    showStats(filesStatus)
