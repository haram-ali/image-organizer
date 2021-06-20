import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from files import get_all_files
from organizer import organize_files




INPUT_DIR = ''
OUT_DIR = ''

ALLOWED_EXTENSIONS = ['.jpg', '.png', '.mp4']
COPY_FILES = True                   # If false then files will be move
USE_FILE_NAME_TO_ORGANIZE = True    # If false then OS attributes will be used


# Getting files
files = get_all_files(
    INPUT_DIR,
    extensions=ALLOWED_EXTENSIONS
)

# Organizing files
organize_files(
    files,
    OUT_DIR,
    copy_files=COPY_FILES,
    use_file_name_to_organize=USE_FILE_NAME_TO_ORGANIZE
)
