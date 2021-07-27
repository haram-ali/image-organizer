from argparse import ArgumentParser

from organizer import organize
from dir_combine import combineDirs
from utilities.chk_extensions import chkExtensions
from utilities.count_files import countFiles
from utilities.are_dirs_same import compareDirs


parser = ArgumentParser()
parser.add_argument(
    'command',
    choices=['organize', 'combine', 'extensions', 'countfiles', 'comparedirs'],
    help='Which script to run'
)


args = parser.parse_args()

if args.command == 'organize':
    organize()
elif args.command == 'combine':
    combineDirs()
elif args.command == 'extensions':
    chkExtensions()
elif args.command == 'countfiles':
    countFiles()
elif args.command == 'comparedirs':
    compareDirs()