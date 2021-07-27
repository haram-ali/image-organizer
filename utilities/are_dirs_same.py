"""
Take multiple directories path and see if the those have same directory stucture.
And also both have same files (by name) & same path (relative).
"""


from private_constants import INPUT_DIRS
from files import getAllFiles


def compareDirs():
    filesByDir = []
    for inputDir in INPUT_DIRS:
        filesByDir.append(getAllFiles(inputDir, relativePath=True))

    allDirsAreSame = True
    for dirFiles in filesByDir:
        if dirFiles != filesByDir[0]:
            allDirsAreSame = False
            break

    print(f'Dirs are {"same" if allDirsAreSame else "not same"}.')
