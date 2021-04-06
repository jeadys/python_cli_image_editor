import sys
import argparse
from PIL import Image
from pathlib import Path
import concurrent.futures
from inspect import cleandoc
from validations.colors import Color
from validations.validator import Validate
# from validations.validator import Validate
from features.convert import Convert


def argument_parser():
    BASE_DIR = Path(__file__).resolve().parent
    INPUT_DIR = BASE_DIR.joinpath('input')

    parent_parser = argparse.ArgumentParser(
        prog='Python CLI Image Editor', description='An application to modify images and more, Made By https://github.com/YassinAO/', add_help=False
    )

    # These commands can be used with any subcommand.
    parent_parser.add_argument('-i', '--input')
    parent_parser.add_argument('-o', '--output')
    parent_parser.add_argument('-b', '--bulk', action='store_true')

    main_parser = argparse.ArgumentParser()

    feature_subparsers = main_parser.add_subparsers(
        help='sub-command help', title='actions', dest='command')  # Dest is defined to see which subcommand is being used.

    convert_parser = feature_subparsers.add_parser(
        'convert', parents=[parent_parser])  # Parent is defined to get access to the parent's commands within this subcommand.

    convert_parser.add_argument('-e', '--extension')

    args = main_parser.parse_args()
    args_dict = vars(args)

    if args.input is None:
        print(cleandoc(f'''
        {Color.WARNING}missing -i OR --input argument{Color.ENDC}'''))
        sys.exit()
    elif args.output is None:
        args.output = BASE_DIR.joinpath('output', args.command)

    Validate(**args_dict).check_path()


if __name__ == '__main__':
    argument_parser()
