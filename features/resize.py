from PIL import Image
from pathlib import Path
import concurrent.futures
Image.warnings.simplefilter('error', Image.DecompressionBombWarning)


class Resize:
    def __init__(self, files, f_output, f_pixels):
        self.files = files
        self.f_output = f_output
        self.f_pixels = f_pixels

    def process_resize(self, file):
        img = Image.open(file)
        new_filename = f'{self.f_pixels}px_{str(file.name)}'
        final_output = self.f_output.joinpath(new_filename)
        dimensions = (self.f_pixels, self.f_pixels)
        img.thumbnail(dimensions, Image.ANTIALIAS)
        img.save(final_output)

    def resize_processor(self):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(self.process_resize, self.files)
