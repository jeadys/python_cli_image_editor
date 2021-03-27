import argparse
from PIL import Image
from colors import Color
from pathlib import Path
from inspect import cleandoc


def argument_parser():
    BASE_DIR = Path(__file__).resolve().parent

    parent_parser = argparse.ArgumentParser(
        prog='Python CLI Image Editor', description='An application to modify images and more, Made By https://github.com/YassinAO/', add_help=False
    )

    # These commands can be used with any subcommand.
    parent_parser.add_argument('-i', '--input')
    parent_parser.add_argument('-o', '--output')
    parent_parser.add_argument('--overwrite', action='store_true')

    main_parser = argparse.ArgumentParser()

    feature_subparsers = main_parser.add_subparsers(
        help='sub-command help', title='actions', dest='command')  # Dest is defined to see which subcommand is being used.

    args = main_parser.parse_args()


if __name__ == '__main__':
    argument_parser()
