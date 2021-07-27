import json

from files import writeToFile


def showStats(filesStatus):
    errFiles = filesStatus['error']

    errExisting = errFiles['exists']
    errInvalidPath = errFiles['invalid_path']
    errOthers = errFiles['other']

    totalSuccessFiles = len(filesStatus['success'])
    totalErrFiles = len(errExisting) + len(errInvalidPath) + len(errOthers)

    if totalErrFiles == 0:
        print('All files files copied/moved successfully.')
        return

    print(f"""
Successfully copied/moved files : {totalSuccessFiles}

Files with error.

    Existing files : {len(errExisting)}
    Invalid path   : {len(errInvalidPath)}
    Other errors   : {len(errOthers)}
    ----------------------
    Total          : {totalErrFiles}

Additional information is stored to {'log.txt'}
    """
)

    writeToFile(
        'log.json',
        json.dumps(filesStatus, indent=2)
    )
