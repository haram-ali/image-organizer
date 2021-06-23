import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from private_constants import INPUT_DIR
from files import get_all_files


files = get_all_files(INPUT_DIR)

print(f'There are {len(files)} file(s).')
