from PIL import Image
from colors import Color
from pathlib import Path
from inspect import cleandoc


def classInfo():
    method_list = [attribute for attribute in dir(Validate) if callable(
        getattr(Validate, attribute)) and attribute.startswith('__') is False]

    for method in method_list:
        print(method)


class Validate(self):
    pass


if __name__ == '__main__':
    classInfo()
