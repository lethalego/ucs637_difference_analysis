import os

from PIL import Image, ImageChops


class Thresholder:

    def apply_threshold(self, image_path, threshold_value):
        image = Image.open(f'{image_path}').convert("L")

        # Yoğunluk farkına göre sınıflandır
        classified = image.point(lambda p: 255 if p > threshold_value else 0, '1')

        # Sınıflandırılmış fark görüntüsünü görüntüle
        nameToSave = os.path.splitext(os.path.basename(image_path))[0] + ".png"
        # Görüntüyü kaydet
        out_file_path = f'Image/7.thresholded'

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        classified.save(f'{out_file_path}/{nameToSave}')
