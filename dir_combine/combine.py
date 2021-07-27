from files import moveFile, copyFile


def combine(files, outDir, copyFiles=True):
    allFilesStatus = {
        'error': {
            'exists': [],
            'invalidPath': [],
            'other': []
        },
        'success': []
    }
    errFiles = allFilesStatus['error']

    for dirFiles in files:
        filesStatus = moveFilesFromDir(dirFiles['files'], dirFiles['input_dir'], outDir, copyFiles)

        errFiles['exists'] += filesStatus['error']['exists']
        errFiles['invalidPath'] += filesStatus['error']['invalidPath']
        errFiles['other'] += filesStatus['error']['other']

        allFilesStatus['success'] += filesStatus['success']

    return allFilesStatus


def moveFilesFromDir(files, inputDir, outDir, copyFiles):
    filesStatus = {
        'error': {
            'exists': [],
            'invalidPath': [],
            'other': []
        },
        'success': []
    }
    errFiles = filesStatus['error']

    moveOrCopy = copyFile if copyFiles else moveFile

    for fileRelativePath in files:
        currPath = f'{inputDir}/{fileRelativePath}'
        newPath = f'{outDir}/{fileRelativePath}'

        err = moveOrCopy(currPath, newPath)

        if err is FileExistsError:
            errFiles['exists'].append(currPath)
        elif err is FileNotFoundError:
            errFiles['invalidPath'].append(currPath)
        elif err is not None:
            errFiles['other'].append(currPath)
        else:
            filesStatus['success'].append(currPath)

    return filesStatus
