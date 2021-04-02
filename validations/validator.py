from PIL import Image
from pathlib import Path
from inspect import cleandoc
from validations.colors import Color
from features.convert import Convert


def classInfo():
    method_list = [attribute for attribute in dir(Validate) if callable(
        getattr(Validate, attribute)) and attribute.startswith('__') is False]

    for method in method_list:
        print(method)


class Validate:
    def __init__(self, **value):
        self.command = value['command']
        self.f_input = Path(value['input'])
        self.f_output = Path(value['output'])
        if self.command == 'convert':
            self.f_extension = value['extension']
        self.bulk = value['bulk']

    def check_path(self):
        Path(self.f_output).mkdir(parents=True, exist_ok=True)

        if (self.f_input.is_dir() and self.bulk or self.f_input.is_file() and not self.bulk) and self.f_output.is_dir():
            print(cleandoc(f'''
            {Color.OKGREEN}valid input/output{Color.ENDC}
            '''))
            return Convert(self.f_input, self.f_output, self.f_extension).convert_processor()
        else:
            print(cleandoc(f'''
            {Color.WARNING}invalid input/output{Color.ENDC}
            '''))


if __name__ == '__main__':
    classInfo()
