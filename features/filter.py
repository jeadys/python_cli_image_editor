from pathlib import Path
from PIL import Image, ImageFilter
from concurrent.futures import ProcessPoolExecutor

from helpers.info import class_info

Image.warnings.simplefilter('error', Image.DecompressionBombWarning)


class Filter:
    def __init__(self, files, f_output, f_blur, optimize):
        self.files = files
        self.f_output = f_output
        self.f_blur = f_blur
        self.optimize = optimize

    def process_filter(self, file):
        img = Image.open(file)
        new_filename = f'blur_{self.f_blur}_{str(file.name)}'
        final_output = self.f_output.joinpath(new_filename)
        img.filter(ImageFilter.GaussianBlur(
            radius=self.f_blur)).save(final_output, optimize=self.optimize, compress_level=9, quality=85)

    def filter_processor(self):
        with ProcessPoolExecutor() as executor:
            executor.map(self.process_filter, self.files)


if __name__ == '__main__':
    class_info(Filter)
