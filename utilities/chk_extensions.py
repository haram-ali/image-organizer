import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from private_constants import INPUT_DIR
from files import get_all_files, get_file_extension


files = get_all_files(INPUT_DIR)
extensions = [get_file_extension(file) for file in files]

# Removing duplicats
extensions = list(dict.fromkeys(extensions))

print(*extensions, sep='\n')
