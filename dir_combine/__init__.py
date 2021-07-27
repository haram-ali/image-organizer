import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from private_constants import INPUT_DIRS, OUT_DIR
from combine import combine
from utilities import showStats
from files import getAllFiles, writeToFile


COPY_FILES = True                   # If false then files will be move


files = []
for inputDir in INPUT_DIRS:
    files.append({
        'input_dir': inputDir,
        'files': getAllFiles(inputDir, relativePath=True)
    })

filesStatus = combine(
    files,
    OUT_DIR,
    copyFiles=COPY_FILES
)

showStats(filesStatus)
