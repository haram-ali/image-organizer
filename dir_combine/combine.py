from files import move_file, copy_file


def combine(files, input_dir_path, out_dir, copy_files=True):
    for file_relative_path in files:
        curr_path = f'{input_dir_path}/{file_relative_path}'
        new_path = f'{out_dir}/{file_relative_path}'

        if copy_files:
            copy_file(curr_path, new_path)
        else:
            move_file(curr_path, new_path)
