import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import json

from private_constants import INPUT_DIRS, OUT_DIR
from combine import combine
from files import get_all_files, write_to_file


COPY_FILES = True                   # If false then files will be move


files = []
for input_dir in INPUT_DIRS:
    files.append({
        'input_dir': input_dir,
        'files': get_all_files(input_dir, relative_path=True)
    })

files_with_err = combine(
    files,
    OUT_DIR,
    copy_files=COPY_FILES
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
