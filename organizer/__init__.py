import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from private_constants import INPUT_DIR, OUT_DIR
from files import get_all_files
from organize import organize_files
from utilities import show_stats


ALLOWED_EXTENSIONS = ['.jpg', '.png', '.mp4']
COPY_FILES = True                   # If false then files will be move
USE_FILE_NAME_TO_ORGANIZE = True    # If false then OS attributes will be used


# Getting files
files = get_all_files(
    INPUT_DIR,
    extensions=ALLOWED_EXTENSIONS
)
print(f'{len(files)} files found.')

# Organizing files
files_status = organize_files(
    files,
    OUT_DIR,
    copy_files=COPY_FILES,
    use_file_name_to_organize=USE_FILE_NAME_TO_ORGANIZE
)

show_stats(files_status)
