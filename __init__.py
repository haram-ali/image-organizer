from argparse import ArgumentParser

from organizer import organize
from dir_combine import combineDirs


parser = ArgumentParser()
parser.add_argument('command', choices=[
                    'organize', 'combine'], help='Which script to run')


args = parser.parse_args()

if args.command == 'organize':
    organize()
elif args.command == 'combine':
    combineDirs()
