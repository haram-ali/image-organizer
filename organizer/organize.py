from datetime import datetime

from files import move_file, copy_file, get_file_name, get_file_path


def organize_files(
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

    move_or_copy = copy_file if copyFiles else move_file
    get_file_date = get_date_from_file_name if useFileNameToOrganize else get_date_from_os_attributes
    def get_file_new_path(fileDate, fileRelativePath):
        fileName = get_file_name(fileRelativePath)
        fileRelativeOnlyPath = get_file_path(fileRelativePath)

        if keepSubDirSutructureInsideDateDirs:
            return f'{outDir}/{fileDate.strftime(r"%Y/%m%B/%d")}/{fileRelativeOnlyPath}/{fileName}'
        else:
            return f'{outDir}/{fileDate.strftime(r"%Y/%m%B/%d")}/{fileName}'

    for fileRelativePath in filesRelativePath:
        fileName = get_file_name(fileRelativePath)
        fileDate = get_file_date(fileName)

        fileCurrPath = f'{inputDir}/{fileRelativePath}'
        fileNewPath = get_file_new_path(fileDate, fileRelativePath)

        err = move_or_copy(fileCurrPath, fileNewPath)

        if err is FileExistsError:
            errFiles['exists'].append(fileCurrPath)
        elif err is FileNotFoundError:
            errFiles['invalid_path'].append(fileCurrPath)
        elif err is not None:
            errFiles['other'].append(fileCurrPath)
        else:
            filesStatus['success'].append(fileCurrPath)

    return filesStatus


def get_date_from_file_name(fileName):
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


def get_date_from_os_attributes(fileName):
    # TODO: Have to implement it
    pass
