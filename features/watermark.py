from pathlib import Path
from PIL import Image, ImageFont
from concurrent.futures import ProcessPoolExecutor

from helpers.info import class_info

"""
The watermark functionality allows the end user to add a watermark to their image(s).
This is done by using the watermark found in the assets folder, this can be replaced.
The image and watermark will be merged together and the watermark will be placed on top of the image.

This can be done in singular and bulk, with the help of multiprocessing technology this feature is sped up by a lot.

Some extra attributes can be passed such as measure and position of the watermark, see README.md for further details.

*IMPORT*
To protect against potential DOS attacks caused by “decompression bombs” 
(i.e. malicious files which decompress into a huge amount of data and are designed to crash or cause disruption by using up a lot of memory), 
Pillow will issue a DecompressionBombWarning if the image is over a certain limit.

This warning is added to the warning filter, to prevent script from stopping due to too many large images.
You can remove the warning from the filter, but for now it's fine because it has no malicious use nor are we accepting images from a malicious user.
"""
Image.warnings.simplefilter('error', Image.DecompressionBombWarning)


class Watermark:
    def __init__(self, files, f_output, f_position, f_size, optimize):
        self.files = files
        self.f_output = f_output
        self.f_position = f_position
        self.v_position, self.h_position = self.f_position.split('_')
        self.f_size = f_size
        self.optimize = optimize
        self.resize = {'small': 8, 'medium': 5, 'large': 3, }

    def process_watermark(self, file):
        img = Image.open(file)
        width_image, height_image = img.size

        watermark = Image.open('assets/watermark.png')

        # To make the watermark fit nicely in the image we scale it down.
        resized_watermark = watermark.thumbnail(
            (width_image / self.resize[self.f_size], width_image / self.resize[self.f_size]), Image.ANTIALIAS)

        width_watermark, height_watermark = watermark.size

        # The width and height of the watermark gets substracted from the image width and height to get the exact corners.
        # Padding is meant for the corners, so the watermark has some whitespace around the edges of the image.
        padding = 50
        positions = {
            'top_left': (padding, padding),
            'top_right': (width_image - width_watermark - padding, padding),
            'bottom_left': (padding, height_image - height_watermark - padding),
            'bottom_right': (width_image - width_watermark - padding, height_image - height_watermark - padding),
        }

        new_filename = f'watermarked_{self.v_position}_{self.h_position}_{str(file.name)}'
        final_output = self.f_output.joinpath(new_filename)

        img.paste(watermark, positions[self.f_position], watermark)
        img.save(final_output, optimize=self.optimize,
                 compress_level=9, quality=85)

    def watermark_processor(self):
        with ProcessPoolExecutor() as executor:
            executor.map(self.process_watermark, self.files)


if __name__ == '__main__':
    class_info(Watermark)
