import json

from files import write_to_file


def show_stats(files_status):
    err_files = files_status['error']

    err_existing = err_files['exists']
    err_invalid_path = err_files['invalid_path']
    err_others = err_files['other']

    total_success_files = len(files_status['success'])
    total_err_files = len(err_existing) + len(err_invalid_path) + len(err_others)

    if total_err_files == 0:
        print('All files files copied/moved successfully.')
        return

    print(f"""
Successfully copied/moved files : {total_success_files}

Files with error.

    Existing files : {len(err_existing)}
    Invalid path   : {len(err_invalid_path)}
    Other errors   : {len(err_others)}
    ----------------------
    Total          : {total_err_files}

Additional information is stored to {'log.txt'}
    """
)

    write_to_file(
        'log.json',
        json.dumps(files_status, indent=2)
    )
