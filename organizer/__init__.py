import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from private_constants import INPUT_DIR, OUT_DIR
from files import get_all_files
from organize import organize_files
from utilities import show_stats


ALLOWED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.mp4']
COPY_FILES = True                   # If false then files will be move
USE_FILE_NAME_TO_ORGANIZE = True    # If false then OS attributes will be used
KEEP_SUB_DIR_SUTRUCTURE_INSIDE_DATE_DIRS = True     # If true then the dir structure will be preserved as in input dir


# Getting files
files = get_all_files(
    INPUT_DIR,
    relativePath=True,
    extensions=ALLOWED_EXTENSIONS
)
print(f'{len(files)} files found.')

# Organizing files
filesStatus = organize_files(
    files,
    INPUT_DIR,
    OUT_DIR,
    copyFiles=COPY_FILES,
    useFileNameToOrganize=USE_FILE_NAME_TO_ORGANIZE,
    keepSubDirSutructureInsideDateDirs=KEEP_SUB_DIR_SUTRUCTURE_INSIDE_DATE_DIRS
)

show_stats(filesStatus)
