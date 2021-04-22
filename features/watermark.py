from pathlib import Path
from PIL import Image, ImageFont
from concurrent.futures import ProcessPoolExecutor

from helpers.info import class_info

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
