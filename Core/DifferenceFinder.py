import io
import os

import numpy as np
from PIL import Image, ImageOps, ImageChops
from skimage import measure


class DifferenceFinder:

    def get_difference(self, image_path_1, image_path_2, combination_name):
        # İlk görüntüyü yükle
        img1 = Image.open(f'{image_path_1}')

        # İkinci görüntüyü yükle
        img2 = Image.open(f'{image_path_2}')

        # İki görüntü arasındaki farkı al
        result = ImageChops.difference(img1, img2)

        name_to_save = os.path.splitext(os.path.basename(image_path_1))[0] + ".png"
        # Görüntüyü kaydet
        out_file_path = f'Image/{combination_name}/6.difference'

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        result.save(f'{out_file_path}/{name_to_save}')

    # Mean Squared Error (MSE)
    def get_difference_MSE(self, image_path_1, image_path_2, combination_name):
        # İlk görüntüyü yükle
        img1 = Image.open(f'{image_path_1}')

        # İkinci görüntüyü yükle
        img2 = Image.open(f'{image_path_2}')

        # Görüntüleri aynı boyuta getir
        img1 = img1.resize(img2.size)

        # Görüntüleri Numpy dizisine dönüştür
        img1_arr = np.array(img1)
        img2_arr = np.array(img2)

        # Piksel farklarını hesapla
        diff = img1_arr.astype(np.float64) - img2_arr.astype(np.float64)

        # Karelerini al ve ortalamasını hesapla
        mse = np.mean(np.square(diff))

        # Sonuçları yazdır
        print(f"Mean Squared Error (MSE): {mse}")

        # Fark görüntüsünü kaydet
        name_to_save = os.path.splitext(os.path.basename(image_path_1))[0] + ".png"
        out_file_path = f'Image/{combination_name}/6.difference'

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        diff_img = Image.fromarray(np.uint8(np.abs(diff)))
        diff_img.save(f'{out_file_path}/{name_to_save}')

