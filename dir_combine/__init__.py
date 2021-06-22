import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from combine import combine
from files import get_all_files


INPUT_DIRS = [
    '',
    ''
]
OUT_DIR = ''

COPY_FILES = True                   # If false then files will be move



for input_dir in INPUT_DIRS:
    # Getting files
    files = get_all_files(input_dir, relative_path=True)

    # Combining
    combine(
        files,
        input_dir,
        OUT_DIR,
        copy_files=COPY_FILES
    )
