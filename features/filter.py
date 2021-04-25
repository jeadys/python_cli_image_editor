from pathlib import Path
from PIL import Image, ImageFilter
from concurrent.futures import ProcessPoolExecutor

#from helpers.info import class_info

"""
The filter functionality allows the end user to add filtering to the image(s)
It allows the end user to add a blur filter by providing an amount in numbers.

This can be done in singular and bulk, with the help of multiprocessing technology this feature is sped up by a lot.

*IMPORT*
To protect against potential DOS attacks caused by “decompression bombs” 
(i.e. malicious files which decompress into a huge amount of data and are designed to crash or cause disruption by using up a lot of memory), 
Pillow will issue a DecompressionBombWarning if the image is over a certain limit.

This warning is added to the warning filter, to prevent script from stopping due to too many large images.
You can remove the warning from the filter, but for now it's fine because it has no malicious use nor are we accepting images from a malicious user.
"""
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
    pass
