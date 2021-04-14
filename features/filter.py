from PIL import Image, ImageFilter
from pathlib import Path
import concurrent.futures
Image.warnings.simplefilter('error', Image.DecompressionBombWarning)


class Filter:
    def __init__(self, files, f_output, f_blur):
        self.files = files
        self.f_output = f_output
        self.f_blur = f_blur

    def process_filter(self, file):
        img = Image.open(file)
        new_filename = f'blur{str(file.name)}'
        final_output = self.f_output.joinpath(new_filename)
        img.filter(ImageFilter.GaussianBlur(
            radius=self.f_blur)).save(final_output)

    def filter_processor(self):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(self.process_filter, self.files)
