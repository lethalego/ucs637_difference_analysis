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
        out_file_path = f'Image/difference'

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        result.save(f'{out_file_path}/{name_to_save}')


        def get_threshold(image_path):
            # Görüntüyü yükle
            img = Image.open(image_path).convert('L')

            # Histogramı hesapla
            histogram, bin_edges = np.histogram(img, bins=256, range=(0, 255))

            # Histogramın birinci türevini hesapla
            diff = np.diff(histogram)

            # En büyük farkın olduğu indeksi bul
            index = np.argmax(diff)

            # Eşik değerini belirle
            threshold = bin_edges[index]

            return threshold


        # Örnek kullanım
        threshold = get_threshold('Image/histogram/before/image1.png')
        print(threshold)