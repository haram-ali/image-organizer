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
            'invalidPath': [],
            'fileNameInvalid': [],
            'other': []
        },
        'success': []
    }
    errFiles = filesStatus['error']

    moveOrCopy = copyFile if copyFiles else moveFile

    for fileRelativePath in filesRelativePath:
        fileCurrPath = f'{inputDir}/{fileRelativePath}'

        try:
            fileDate = getFileDate(fileRelativePath, useFileNameToOrganize)
        except:
            errFiles['fileNameInvalid'].append(fileCurrPath)
            continue

        fileNewPath = getFileNewPath(fileDate, fileRelativePath, outDir, keepSubDirSutructureInsideDateDirs)

        err = moveOrCopy(fileCurrPath, fileNewPath)

        if err is FileExistsError:
            errFiles['exists'].append(fileCurrPath)
        elif err is FileNotFoundError:
            errFiles['invalidPath'].append(fileCurrPath)
        elif err is not None:
            errFiles['other'].append(fileCurrPath)
        else:
            filesStatus['success'].append(fileCurrPath)

    return filesStatus


def getFileNewPath(fileDate, fileRelativePath, outDir, keepSubDirSutructureInsideDateDirs):
        fileName = getFileName(fileRelativePath)
        fileRelativeOnlyPath = getFilePath(fileRelativePath)

        if keepSubDirSutructureInsideDateDirs:
            return f'{outDir}/{fileDate.strftime(r"%Y/%m%B/%d")}/{fileRelativeOnlyPath}/{fileName}'
        else:
            return f'{outDir}/{fileDate.strftime(r"%Y/%m%B/%d")}/{fileName}'


def getFileDate(file, useFileNameToOrganize):
    fileName = getFileName(file)

    if useFileNameToOrganize:
        return getDateFromFileName(fileName)
    else:
        return getDateFromOsAttributes(fileName)


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
