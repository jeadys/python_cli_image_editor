from PIL import Image
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor

from helpers.info import class_info

"""
The dimension functionality allows the end user to change the dimension of the image(s).
It allows the end user to scale the image(s) by providing the pixels.
It allows the end user to rotate the image(s) by providing the degree.
It allows the end user to flip the image(s) by providing the direction (vertical, horizontal).

This can be done in singular and bulk, with the help of multiprocessing technology this feature is sped up by a lot.

*IMPORT*
To protect against potential DOS attacks caused by “decompression bombs” 
(i.e. malicious files which decompress into a huge amount of data and are designed to crash or cause disruption by using up a lot of memory), 
Pillow will issue a DecompressionBombWarning if the image is over a certain limit.

This warning is added to the warning filter, to prevent script from stopping due to too many large images.
You can remove the warning from the filter, but for now it's fine because it has no malicious use nor are we accepting images from a malicious user.
"""
Image.warnings.simplefilter('error', Image.DecompressionBombWarning)


class Dimension:
    def __init__(self, files, f_output, f_scale, f_rotate, f_flip, optimize):
        self.files = files
        self.f_output = f_output
        self.f_scale = f_scale
        self.f_rotate = f_rotate
        self.f_flip = f_flip
        self.optimize = optimize

    def process_dimension(self, file):
        img = Image.open(file)

        if self.f_scale:
            new_filename = f'{self.f_scale}px_{str(file.name)}'
            dimensions = (self.f_scale, self.f_scale)
            final_edit = img.thumbnail(dimensions, Image.ANTIALIAS)
        elif self.f_rotate:
            new_filename = f'{self.f_rotate}degree_{str(file.name)}'
            final_edit = img.rotate(self.f_rotate)
        elif self.f_flip:
            new_filename = f'{self.f_flip}_flip_{str(file.name)}'
            final_edit = img.transpose(method=Image.FLIP_TOP_BOTTOM) if self.f_flip == 'vertical' else img.transpose(
                method=Image.FLIP_LEFT_RIGHT)

        final_output = self.f_output.joinpath(new_filename)
        final_edit.save(final_output, optimize=self.optimize,
                        compress_level=9, quality=85)

    def dimension_processor(self):
        with ProcessPoolExecutor() as executor:
            executor.map(self.process_dimension, self.files)


if __name__ == '__main__':
    class_info(Dimension)
