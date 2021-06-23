import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import json

from private_constants import INPUT_DIRS, OUT_DIR
from combine import combine
from utilities import show_stats
from files import get_all_files, write_to_file


COPY_FILES = True                   # If false then files will be move


files = []
for input_dir in INPUT_DIRS:
    files.append({
        'input_dir': input_dir,
        'files': get_all_files(input_dir, relative_path=True)
    })

files_status = combine(
    files,
    OUT_DIR,
    copy_files=COPY_FILES
)

show_stats(files_status)
