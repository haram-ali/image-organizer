from datetime import datetime

from files import move_file, copy_file, get_file_name


def organize_files(
    files,
    out_dir,
    copy_files=True,
    use_file_name_to_organize=True
):
    files_status = {
        'error': {
            'exists': [],
            'invalid_path': [],
            'other': []
        },
        'success': []
    }
    err_files = files_status['error']

    move_or_copy = copy_file if copy_files else move_file

    for file_curr_path in files:
        file_name = get_file_name(file_curr_path)

        file_date = None
        if use_file_name_to_organize:
            file_date = get_date_from_file_name(file_name)
        else:
            file_date = get_date_from_os_attributes(file_name)

        file_new_path = f'{out_dir}/{file_date.strftime(r"%Y/%m%B/%d")}/{file_name}'

        err = move_or_copy(file_curr_path, file_new_path)

        if err is FileExistsError:
            err_files['exists'].append(file_curr_path)
        elif err is FileNotFoundError:
            err_files['invalid_path'].append(file_curr_path)
        elif err is not None:
            err_files['other'].append(file_curr_path)
        else:
            files_status['success'].append(file_curr_path)

    return files_status


def get_date_from_file_name(file_name):
    # Example file names:
    #   IMG-20210105-WA0036.jpg

    #   VID_20210207_205658.mp4
    #   VID-20210613-WA0039.mp4

    date_str = file_name[4:12]  # 20210105

    year = int(date_str[0:4])   # 2021
    month = int(date_str[4:6])  # 01
    day = int(date_str[6:])     # 05

    return datetime(year, month, day)


def get_date_from_os_attributes(file_name):
    # TODO: Have to implement it
    pass
