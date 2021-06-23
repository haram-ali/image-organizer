from files import move_file, copy_file


def combine(files, out_dir, copy_files=True):
    all_files_status = {
        'error': {
            'exists': [],
            'invalid_path': [],
            'other': []
        },
        'success': []
    }
    err_files = all_files_status['error']

    for a in files:
        files_status = move_files_from_dir(a['files'], a['input_dir'], out_dir, copy_files)

        err_files['exists'] += files_status['error']['exists']
        err_files['invalid_path'] += files_status['error']['invalid_path']
        err_files['other'] += files_status['error']['other']

        all_files_status['success'] += files_status['success']

    return all_files_status


def move_files_from_dir(files, input_dir, out_dir, copy_files):
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

    for file_relative_path in files:
        curr_path = f'{input_dir}/{file_relative_path}'
        new_path = f'{out_dir}/{file_relative_path}'

        err = move_or_copy(curr_path, new_path)

        if err is FileExistsError:
            err_files['exists'].append(curr_path)
        elif err is FileNotFoundError:
            err_files['invalid_path'].append(curr_path)
        elif err is not None:
            err_files['other'].append(curr_path)
        else:
            files_status['success'].append(curr_path)

    return files_status
