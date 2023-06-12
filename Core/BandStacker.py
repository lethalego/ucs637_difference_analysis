import os

import numpy as np

from PIL import Image

from Core.BandCombinator import BandCombinator


class BandStacker:

    def stack_bands_into_one_true_color_image(self, before_after, image_path, combination_name):
        """
        gets tiff image, combine band 4 3 2 and returns a brightened true color image in format png
        """
        bandCombinator = BandCombinator()

        combined = bandCombinator.combine(image_path, combination_name)

        # Numpy dizisini PIL görüntüsüne dönüştür
        image = Image.fromarray(np.uint8(combined))

        nameToSave = os.path.splitext(os.path.basename(image_path))[0] + ".png"

        # Görüntüyü kaydet
        out_file_path = f'Image/{combination_name}/3.stack/{before_after}'

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        image.save(f'{out_file_path}/{nameToSave}')
