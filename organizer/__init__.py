import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import json

from private_constants import INPUT_DIR, OUT_DIR
from files import get_all_files, write_to_file
from organizer import organize_files


ALLOWED_EXTENSIONS = ['.jpg', '.png', '.mp4']
COPY_FILES = True                   # If false then files will be move
USE_FILE_NAME_TO_ORGANIZE = True    # If false then OS attributes will be used


# Getting files
files = get_all_files(
    INPUT_DIR,
    extensions=ALLOWED_EXTENSIONS
)
print(f'{len(files)} files found.')

# Organizing files
files_with_err = organize_files(
    files,
    OUT_DIR,
    copy_files=COPY_FILES,
    use_file_name_to_organize=USE_FILE_NAME_TO_ORGANIZE
)

print(f"""
Files with error in {'copying' if COPY_FILES else 'moving'}.

    Existing files : {len(files_with_err['exists'])}
    Invalid path   : {len(files_with_err['invalid_path'])}
    Other errors   : {len(files_with_err['other'])}
    ----------------------
    Total          : {len(files_with_err['exists'])+len(files_with_err['invalid_path'])+len(files_with_err['other'])}

Additional information is stored to {'file.txt'}
"""
)

write_to_file('error-log.txt', json.dumps(files_with_err, indent=2))
