import os

from PIL import Image, ImageOps
import numpy as np
from skimage import exposure


class Normalyzer:

    def normalyze_min_max(self, before_after, image_path, combination_name):
        image = Image.open(f'{image_path}').convert("L")
        image_array = np.array(image)

        normalized_image = (image_array - np.min(image_array)) / (np.max(image_array) - np.min(image_array))
        normalized_image = (normalized_image * 255).astype(np.uint8)
        normalized_image = Image.fromarray(normalized_image)

        nameToSave = os.path.splitext(os.path.basename(image_path))[0] + ".png"
        # Görüntüyü kaydet
        out_file_path = f'Image/{combination_name}/4.normalyzed/{before_after}'

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        normalized_image.save(f'{out_file_path}/{nameToSave}')

    def normalize_z_score(self, before_after, image_path, combination_name):
        image = Image.open(f'{image_path}').convert("L")
        image_array = np.array(image)

        # Z-score normalization
        normalized_image = (image_array - np.mean(image_array)) / np.std(image_array)
        normalized_image = (normalized_image * 255).astype(np.uint8)
        normalized_image = Image.fromarray(normalized_image)

        # Dosya adını oluştur
        nameToSave = os.path.splitext(os.path.basename(image_path))[0] + ".png"
        # Görüntüyü kaydet
        out_file_path = f'Image/{combination_name}/4.normalyzed/{before_after}'

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        normalized_image.save(f'{out_file_path}/{nameToSave}')

    def normalize_clahe(self, before_after, image_path, combination_name):
        # Resmi yükle ve dönüştür
        image = Image.open(f'{image_path}').convert("L")
        image_array = np.array(image)

        # CLAHE algoritması uygula
        normalized_image = exposure.equalize_adapthist(image_array, clip_limit=0.03)

        # 0-255 arasına ölçekle
        normalized_image = (normalized_image * 255).astype(np.uint8)
        normalized_image = Image.fromarray(normalized_image)

        # Dosya adını hazırla ve kaydet
        nameToSave = os.path.splitext(os.path.basename(image_path))[0] + ".png"
        out_file_path = f'Image/{combination_name}/4.normalyzed/{before_after}'

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        normalized_image.save(f'{out_file_path}/{nameToSave}')

    #Global Histogram Normalleştirme
    def normalyze_histogram(self, before_after, image_path, combination_name):
        image = Image.open(f'{image_path}')
        image_array = np.array(image)

        image = Image.fromarray(image_array)

        result = ImageOps.equalize(image)

        name_to_save = os.path.splitext(os.path.basename(image_path))[0] + ".png"
        # Görüntüyü kaydet
        out_file_path = f'Image/{combination_name}/5.histogram/{before_after}'

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        result.save(f'{out_file_path}/{name_to_save}')

