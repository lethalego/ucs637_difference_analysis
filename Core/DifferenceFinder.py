import os

import numpy as np
from PIL import Image, ImageOps, ImageChops


class DifferenceFinder:

    def get_difference(self, image_path_1, image_path_2):
        # İlk görüntüyü yükle
        img1 = Image.open(f'{image_path_1}')

        # İkinci görüntüyü yükle
        img2 = Image.open(f'{image_path_2}')

        # İki görüntü arasındaki farkı al
        result = ImageChops.difference(img1, img2)

        name_to_save = os.path.splitext(os.path.basename(image_path_1))[0] + ".png"
        # Görüntüyü kaydet
        out_file_path = f'Image/6.difference'

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        result.save(f'{out_file_path}/{name_to_save}')
