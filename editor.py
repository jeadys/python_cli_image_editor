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

    # add_mutually_exclusive_group is to prevent multiple arguments being used for a subcommand.

    convert_parser = feature_subparsers.add_parser(
        'convert', parents=[parent_parser])
    convert_parser.add_argument('-e', '--extension')

    dimension_parser = feature_subparsers.add_parser(
        'dimension', parents=[parent_parser])
    dimension_parser = dimension_parser.add_mutually_exclusive_group()
    dimension_parser.add_argument('--scale', type=int)
    dimension_parser.add_argument('--rotate', type=int)
    dimension_parser.add_argument(
        '--flip', type=str, choices=['vertical', 'horizontal'])

    filter_parser = feature_subparsers.add_parser(
        'filter', parents=[parent_parser])
    filter_parser = filter_parser.add_mutually_exclusive_group()
    filter_parser.add_argument('--blur', type=int, nargs='?',
                               default=None, const=None)

    hue_parser = feature_subparsers.add_parser(
        'hue', parents=[parent_parser])
    hue_parser = hue_parser.add_mutually_exclusive_group()
    hue_parser.add_argument('--contrast', type=float)
    hue_parser.add_argument('--monochrome', action='store_true')

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
