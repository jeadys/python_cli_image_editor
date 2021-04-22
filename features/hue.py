from pathlib import Path
from PIL import Image, ImageEnhance
from concurrent.futures import ProcessPoolExecutor

from helpers.info import class_info

Image.warnings.simplefilter('error', Image.DecompressionBombWarning)


class Hue:
    def __init__(self, files, f_output, f_contrast, f_monochrome, optimize):
        self.files = files
        self.f_output = f_output
        self.f_contrast = f_contrast
        self.f_monochrome = f_monochrome
        self.optimize = optimize

    def process_hue(self, file):
        img = Image.open(file)

        if self.f_contrast:
            new_filename = f'contrast_{str(file.name)}'
            enhancer = ImageEnhance.Contrast(img)
            final_edit = enhancer.enhance(self.f_contrast)
        elif self.f_monochrome:
            new_filename = f'monochrome_{str(file.name)}'
            final_edit = img.convert(mode='L')

        final_output = self.f_output.joinpath(new_filename)
        final_edit.save(final_output, optimize=self.optimize,
                        compress_level=9, quality=85)

    def hue_processor(self):
        with ProcessPoolExecutor() as executor:
            executor.map(self.process_hue, self.files)


if __name__ == '__main__':
    class_info(Hue)
