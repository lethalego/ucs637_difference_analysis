import os

import numpy as np
import rasterio

from PIL import Image


class BandStacker:

    def stack_bands_into_one_true_color_image(self, before_after, image_path):
        """
        gets tiff image, combine band 4 3 2 and returns a brightened true color image in format png
        """
        with rasterio.open(image_path) as src:
            # Display the masked image

            BLUE_BAND = 2
            GREEN_BAND = 3
            RED_BAND = 4

            red = src.read(RED_BAND)
            green = src.read(GREEN_BAND)
            blue = src.read(BLUE_BAND)

            # Piksel değerlerini 2.5 ile çarpıp parlaklığı artır
            red = np.multiply(red, 2.5)
            green = np.multiply(green, 2.5)
            blue = np.multiply(blue, 2.5)

            # Piksel değerlerini 0-255 aralığına sınırla
            red = np.clip(red, 0, 255)
            green = np.clip(green, 0, 255)
            blue = np.clip(blue, 0, 255)

            # RGB kanallarını birleştir
            rgb = np.dstack((red, green, blue))

            # Numpy dizisini PIL görüntüsüne dönüştür
            image = Image.fromarray(np.uint8(rgb))

            nameToSave = os.path.splitext(os.path.basename(image_path))[0] + ".png"

            # Görüntüyü kaydet
            out_file_path = f'Image/stack/{before_after}'

            if not os.path.exists(out_file_path):
                os.makedirs(out_file_path)

            image.save(f'{out_file_path}/{nameToSave}')
