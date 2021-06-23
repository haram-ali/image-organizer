"""
Take multiple directories path and see if the those have same directory stucture.
And also both have same files (by name) & same path (relative).
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from private_constants import INPUT_DIRS
from files import get_all_files


files_by_dir = []
for input_dir in INPUT_DIRS:
    files_by_dir.append(get_all_files(input_dir, relative_path=True))

all_dirs_are_same = True
for dir_files in files_by_dir:
    if dir_files != files_by_dir[0]:
        all_dirs_are_same = False
        break

print(f'Dirs are {"same" if all_dirs_are_same else "not same"}.')
