from PIL import Image
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor

Image.warnings.simplefilter('error', Image.DecompressionBombWarning)


class Convert:
    def __init__(self, files, f_output, f_extension, optimize):
        self.files = files
        self.f_output = f_output
        self.f_extension = f_extension
        self.optimize = optimize

    def process_convert(self, file):
        img = Image.open(file)
        new_filename = str(file.name).replace(
            str(file.suffix), self.f_extension)
        final_output = self.f_output.joinpath(new_filename)
        img.save(final_output, optimize=self.optimize,
                 compress_level=9, quality=85)

    def convert_processor(self):
        with ProcessPoolExecutor() as executor:
            executor.map(self.process_convert, self.files)
