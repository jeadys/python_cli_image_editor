from PIL import Image
from pathlib import Path
import concurrent.futures
Image.warnings.simplefilter('error', Image.DecompressionBombWarning)


class Convert:
    def __init__(self, f_input, f_output, f_extension):
        self.f_input = f_input
        self.f_output = f_output
        self.f_extension = f_extension
        self.image_extensions = ['.jpg', '.jpeg', '.png']
        self.files = [x for x in Path(self.f_input).glob(
            '*') if x.suffix in self.image_extensions and self.f_extension != x.suffix]

    # fix this code
    def process_convert(self, file):
        img = Image.open(file)
        new_filename = str(file.name).replace(
            str(file.suffix), self.f_extension)
        final_output = self.f_output.joinpath(new_filename)
        img.save(final_output)

    def convert_processor(self):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(self.process_convert, self.files)
