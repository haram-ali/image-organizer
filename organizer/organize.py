from datetime import datetime

from files import moveFile, copyFile, getFileName, getFilePath


def organizeFiles(
    filesRelativePath,
    inputDir,
    outDir,
    copyFiles=True,
    useFileNameToOrganize=True,
    keepSubDirSutructureInsideDateDirs=False
):
    filesStatus = {
        'error': {
            'exists': [],
            'invalid_path': [],
            'other': []
        },
        'success': []
    }
    errFiles = filesStatus['error']

    moveOrCopy = copyFile if copyFiles else moveFile
    getFileDate = getDateFromFileName if useFileNameToOrganize else getDateFromOsAttributes
    def getFileNewPath(fileDate, fileRelativePath):
        fileName = getFileName(fileRelativePath)
        fileRelativeOnlyPath = getFilePath(fileRelativePath)

        if keepSubDirSutructureInsideDateDirs:
            return f'{outDir}/{fileDate.strftime(r"%Y/%m%B/%d")}/{fileRelativeOnlyPath}/{fileName}'
        else:
            return f'{outDir}/{fileDate.strftime(r"%Y/%m%B/%d")}/{fileName}'

    for fileRelativePath in filesRelativePath:
        fileName = getFileName(fileRelativePath)
        fileDate = getFileDate(fileName)

        fileCurrPath = f'{inputDir}/{fileRelativePath}'
        fileNewPath = getFileNewPath(fileDate, fileRelativePath)

        err = moveOrCopy(fileCurrPath, fileNewPath)

        if err is FileExistsError:
            errFiles['exists'].append(fileCurrPath)
        elif err is FileNotFoundError:
            errFiles['invalid_path'].append(fileCurrPath)
        elif err is not None:
            errFiles['other'].append(fileCurrPath)
        else:
            filesStatus['success'].append(fileCurrPath)

    return filesStatus


def getDateFromFileName(fileName):
    # Example file names:
    #   IMG-20210105-WA0036.jpg
    #   Screenshot_20210622_210602_com.whatsapp.jpg

    #   VID_20210207_205658.mp4
    #   VID-20210613-WA0039.mp4

    dateStr = None
    if 'Screenshot' in fileName:
        dateStr = fileName[11:19]   # 20210105
    else:
        dateStr = fileName[4:12]    # 20210105

    year = int(dateStr[0:4])   # 2021
    month = int(dateStr[4:6])  # 01
    day = int(dateStr[6:])     # 05

    return datetime(year, month, day)


def getDateFromOsAttributes(fileName):
    # TODO: Have to implement it
    pass
