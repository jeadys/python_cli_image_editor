from PIL import Image
from pathlib import Path
import concurrent.futures
Image.warnings.simplefilter('error', Image.DecompressionBombWarning)


class Convert:
    def __init__(self, files, f_output, f_extension):
        self.files = files
        self.f_output = f_output
        self.f_extension = f_extension

    def process_convert(self, file):
        img = Image.open(file)
        new_filename = str(file.name).replace(
            str(file.suffix), self.f_extension)
        final_output = self.f_output.joinpath(new_filename)
        img.save(final_output)

    def convert_processor(self):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(self.process_convert, self.files)
