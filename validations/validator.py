from PIL import Image
from pathlib import Path
from inspect import cleandoc
from validations.colors import Color
from features.convert import Convert
from features.dimension import Dimension
from features.filter import Filter
from features.hue import Hue


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
        if self.command == 'dimension':
            self.f_scale = value['scale']
            self.f_rotate = value['rotate']
        if self.command == 'filter':
            self.f_blur = value['blur']
        if self.command == 'hue':
            self.f_contrast = value['contrast']
            self.f_monochrome = value['monochrome']
        self.bulk = value['bulk']
        self.optimize = value['optimize']

    def check_path(self):
        Path(self.f_output).mkdir(parents=True, exist_ok=True)

        if (self.f_input.is_dir() and self.bulk or self.f_input.is_file() and not self.bulk) and self.f_output.is_dir():
            print(cleandoc(f'''
            {Color.OKGREEN}valid input/output{Color.ENDC}
            '''))
            return self.check_extension()
        else:
            print(cleandoc(f'''
            {Color.WARNING}invalid input/output{Color.ENDC}
            '''))

    def check_extension(self):
        image_extensions = ['jpg', '.jpg', 'jpeg', '.jpeg', '.png', 'png']

        files = [self.f_input] if not self.bulk else [file for file in Path(self.f_input).glob(
            '*') if file.suffix in image_extensions]  # and self.f_extension != file.suffix

        if self.command == 'convert':
            # This is to prevent convertion from -> to same file extension (saves processing time).
            files = [file for file in files if self.f_extension != file.suffix]
            return Convert(files, self.f_output, self.f_extension, self.optimize).convert_processor()
        elif self.command == 'dimension':
            return Dimension(files, self.f_output, self.f_scale, self.f_rotate, self.optimize).dimension_processor()
        elif self.command == 'filter':
            return Filter(files, self.f_output, self.f_blur, self.optimize).filter_processor()
        elif self.command == 'hue':
            return Hue(files, self.f_output, self.f_contrast, self.f_monochrome, self.optimize).hue_processor()
        else:
            return False


if __name__ == '__main__':
    classInfo()
