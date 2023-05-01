import os

from PIL import Image, ImageOps
import numpy as np


class Normalyzer:

    def mormalyze_min_max(self, before_after, image_path):
        image = Image.open(f'{image_path}').convert("L")
        image_array = np.array(image)

        normalized_image = (image_array - np.min(image_array)) / (np.max(image_array) - np.min(image_array))
        normalized_image = (normalized_image * 255).astype(np.uint8)
        normalized_image = Image.fromarray(normalized_image)

        nameToSave = os.path.splitext(os.path.basename(image_path))[0] + ".png"
        # Görüntüyü kaydet
        out_file_path = f'Image/normalyzed/{before_after}'

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        normalized_image.save(f'{out_file_path}/{nameToSave}')

    def normalyze_histogram(self, before_after, image_path):
        image = Image.open(f'{image_path}')
        image_array = np.array(image)

        image = Image.fromarray(image_array)

        result = ImageOps.equalize(image)

        name_to_save = os.path.splitext(os.path.basename(image_path))[0] + ".png"
        # Görüntüyü kaydet
        out_file_path = f'Image/histogram/{before_after}'

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        result.save(f'{out_file_path}/{name_to_save}')
