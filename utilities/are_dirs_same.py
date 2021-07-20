"""
Take multiple directories path and see if the those have same directory stucture.
And also both have same files (by name) & same path (relative).
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from private_constants import INPUT_DIRS
from files import get_all_files


filesByDir = []
for input_dir in INPUT_DIRS:
    filesByDir.append(get_all_files(input_dir, relative_path=True))

allDirsAreSame = True
for dir_files in filesByDir:
    if dir_files != filesByDir[0]:
        allDirsAreSame = False
        break

print(f'Dirs are {"same" if allDirsAreSame else "not same"}.')
