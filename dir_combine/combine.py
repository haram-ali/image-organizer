from files import move_file, copy_file


def combine(files, outDir, copyFiles=True):
    allFilesStatus = {
        'error': {
            'exists': [],
            'invalid_path': [],
            'other': []
        },
        'success': []
    }
    errFiles = allFilesStatus['error']

    for dirFiles in files:
        files_status = move_files_from_dir(dirFiles['files'], dirFiles['input_dir'], outDir, copyFiles)

        errFiles['exists'] += files_status['error']['exists']
        errFiles['invalid_path'] += files_status['error']['invalid_path']
        errFiles['other'] += files_status['error']['other']

        allFilesStatus['success'] += files_status['success']

    return allFilesStatus


def move_files_from_dir(files, inputDir, outDir, copyFiles):
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

    for fileRelativePath in files:
        currPath = f'{inputDir}/{fileRelativePath}'
        newPath = f'{outDir}/{fileRelativePath}'

        err = move_or_copy(currPath, newPath)

        if err is FileExistsError:
            errFiles['exists'].append(currPath)
        elif err is FileNotFoundError:
            errFiles['invalid_path'].append(currPath)
        elif err is not None:
            errFiles['other'].append(currPath)
        else:
            filesStatus['success'].append(currPath)

    return filesStatus
