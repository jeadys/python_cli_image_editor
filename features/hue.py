from pathlib import Path
from PIL import Image, ImageEnhance
from concurrent.futures import ProcessPoolExecutor

from helpers.info import class_info

"""
The hue functionality allows the end user to change the coloring of the image(s).
It allows the end user to add/remove contrast from the image(s) by providing an amount in numbers.
It allows the end user to turn the image(s) black and white.

This can be done in singular and bulk, with the help of multiprocessing technology this feature is sped up by a lot.

*IMPORT*
To protect against potential DOS attacks caused by “decompression bombs” 
(i.e. malicious files which decompress into a huge amount of data and are designed to crash or cause disruption by using up a lot of memory), 
Pillow will issue a DecompressionBombWarning if the image is over a certain limit.

This warning is added to the warning filter, to prevent script from stopping due to too many large images.
You can remove the warning from the filter, but for now it's fine because it has no malicious use nor are we accepting images from a malicious user.
"""
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
