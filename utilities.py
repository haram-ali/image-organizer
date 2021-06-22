import json

from files import write_to_file


def show_stats(files_with_err):
    existing = files_with_err['exists']
    invalid_path = files_with_err['invalid_path']
    others = files_with_err['other']

    total_files = len(existing) + len(invalid_path) + len(others)

    if total_files == 0:
        print('All files files copied/moved successfully.')
        return

    print(f"""
Files with error.

    Existing files : {len(existing)}
    Invalid path   : {len(invalid_path)}
    Other errors   : {len(others)}
    ----------------------
    Total          : {total_files}

Additional information is stored to {'file.txt'}
    """
)

    write_to_file(
        'error-log.txt',
        json.dumps(files_with_err, indent=2)
    )
