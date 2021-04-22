from PIL import Image
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor

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
