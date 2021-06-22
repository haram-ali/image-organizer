from files import move_file, copy_file


def combine(files, out_dir, copy_files=True):
    total_files_with_err = {
        'exists': [],
        'invalid_path': [],
        'other': []
    }

    for a in files:
        files_with_err = move_files_from_dir(a['files'], a['input_dir'], out_dir, copy_file)

        total_files_with_err['exists'] += files_with_err['exists']
        total_files_with_err['invalid_path'] += files_with_err['invalid_path']
        total_files_with_err['other'] += files_with_err['other']

    return total_files_with_err


def move_files_from_dir(files, input_dir, out_dir, copy_files):
    files_with_err = {
        'exists': [],
        'invalid_path': [],
        'other': []
    }
    
    move_or_copy = copy_file if copy_files else move_file
    
    for file_relative_path in files:
        curr_path = f'{input_dir}/{file_relative_path}'
        new_path = f'{out_dir}/{file_relative_path}'

        err = move_or_copy(curr_path, new_path)

        if err is FileExistsError:
            files_with_err['exists'].append(curr_path)
        elif err is FileNotFoundError:
            files_with_err['invalid_path'].append(curr_path)
        elif err is not None:
            files_with_err['other'].append(curr_path)

    return files_with_err
