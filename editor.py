import sys
import argparse
from PIL import Image
from pathlib import Path
import concurrent.futures
from inspect import cleandoc
from validations.colors import Color
from validations.validator import Validate
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
    parent_parser.add_argument('--optimize', action='store_true')

    main_parser = argparse.ArgumentParser()

    feature_subparsers = main_parser.add_subparsers(
        help='sub-command help', title='actions', dest='command')  # Dest is defined to see which subcommand is being used.

    # Some arguments within the subcommand have nargs, default & const defined.
    # nargs is for 0 or 1 argument expected.
    # default is used when argument isn't specified.
    # const is used when argument is specified but no value given.

    # Each subparser (subcommand) has parent defined to get access to the parent's commands within that subparser (subcommand).

    convert_parser = feature_subparsers.add_parser(
        'convert', parents=[parent_parser])
    convert_parser.add_argument('-e', '--extension')

    resize_parser = feature_subparsers.add_parser(
        'resize', parents=[parent_parser])
    resize_parser.add_argument('-p', '--pixels', type=int)

    filter_parser = feature_subparsers.add_parser(
        'filter', parents=[parent_parser])
    # This is to prevent multiple arguments being used for the filter subcommand.
    filter_parser = filter_parser.add_mutually_exclusive_group()
    filter_parser.add_argument('--blur', type=int, nargs='?',
                               default=15, const=15)

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
