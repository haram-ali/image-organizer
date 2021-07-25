import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from private_constants import INPUT_DIRS, OUT_DIR
from combine import combine
from utilities import show_stats
from files import get_all_files, write_to_file


COPY_FILES = True                   # If false then files will be move


files = []
for inputDir in INPUT_DIRS:
    files.append({
        'input_dir': inputDir,
        'files': get_all_files(inputDir, relativePath=True)
    })

files_status = combine(
    files,
    OUT_DIR,
    copyFiles=COPY_FILES
)

show_stats(files_status)
