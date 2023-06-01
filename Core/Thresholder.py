import os

import cv2
import numpy as np
from PIL import Image, ImageChops, ImageFilter


class Thresholder:

    def apply_threshold(self, image_path, threshold_value, combination_name):
        image = Image.open(f'{image_path}').convert("L")

        # Yoğunluk farkına göre sınıflandır
        classified = image.point(lambda p: 255 if p > threshold_value else 0, '1')

        # Sınıflandırılmış fark görüntüsünü görüntüle
        nameToSave = os.path.splitext(os.path.basename(image_path))[0] + ".png"
        # Görüntüyü kaydet
        out_file_path = f'Image/{combination_name}/7.thresholded'

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        classified.save(f'{out_file_path}/{nameToSave}')

    def apply_threshold_otsu(self, image_path, combination_name):
        # Görüntüyü yükle ve gri tonlamalı hale getir
        img = Image.open(f'{image_path}').convert('L')

        img_array = np.array(img)

        # Histogramı hesapla
        hist, _ = np.histogram(img_array, bins=256)

        # Toplam piksel sayısını hesapla
        total_pixels = img_array.shape[0] * img_array.shape[1]

        # Piksel olasılıklarını hesapla
        pixel_probabilities = hist / total_pixels

        # Sınıf olasılıklarını hesapla
        class_probabilities = np.zeros(256)
        class_probabilities[0] = pixel_probabilities[0]
        for i in range(1, 256):
            class_probabilities[i] = class_probabilities[i - 1] + pixel_probabilities[i]

        # Sınıf ortalamalarını hesapla
        class_means = np.zeros(256)
        class_means[0] = 0
        for i in range(1, 256):
            class_means[i] = class_means[i - 1] + i * pixel_probabilities[i]

        # Toplam ortalama ve sınıf varyansını hesapla

        epsilon = 1e-10  # Küçük bir değer (eps) eklendi

        total_mean = np.sum(np.arange(256) * pixel_probabilities)
        between_class_variances = (total_mean * class_probabilities - class_means) ** 2 / (
                class_probabilities * (1 - class_probabilities + epsilon))

        # Eşik değerini Otsu yöntemine göre belirle
        threshold_value = np.argmax(between_class_variances)

        # Eşik değerini kullanarak sınıflandır
        binary_image = np.zeros_like(img_array)
        binary_image[img_array > threshold_value] = 255

        # Sınıflandırılmış görüntüyü kaydet
        classified = Image.fromarray(binary_image)

        # Sınıflandırılmış fark görüntüsünü görüntüle
        nameToSave = os.path.splitext(os.path.basename(image_path))[0] + ".png"
        # Görüntüyü kaydet
        out_file_path = f'Image/{combination_name}/7.thresholded'

        # print(f'{nameToSave}(threshold): {threshold_value} ')
        #print(f'{threshold_value} ')

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        classified.save(f'{out_file_path}/{nameToSave}')

    def apply_threshold_gaussian(self, image_path, combination_name):

        image = Image.open(f'{image_path}').convert("L")
        # Resmi bir NumPy dizisine dönüştür
        image_array = np.array(image)

        # Resimdeki tüm piksellerin ortalama değerini ve standart sapmasını hesapla
        mean_value = np.mean(image_array)
        std_dev = np.std(image_array)

        # Threshold değerini hesapla
        threshold_value = mean_value + 2 * std_dev

        # Resmi threshold değeriyle sınıflandır
        classified = np.where(image_array > threshold_value, 255, 0)

        # Sınıflandırılmış resmi bir PIL görüntüsüne dönüştür
        result = Image.fromarray(classified.astype('uint8'))

        # Sınıflandırılmış fark görüntüsünü görüntüle
        nameToSave = os.path.splitext(os.path.basename(image_path))[0] + ".png"
        # Görüntüyü kaydet
        out_file_path = f'Image/{combination_name}/7.thresholded'

        # print(f'{nameToSave}(threshold): {threshold_value} ')
        #print(f'{threshold_value} ')

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        result.save(f'{out_file_path}/{nameToSave}')

    def apply_mean_threshold(self, image_path, combination_name):
        image = Image.open(f'{image_path}').convert("L")
        # Resmi bir NumPy dizisine dönüştür
        image_array = np.array(image)

        # Resimdeki tüm piksellerin ortalama değerini ve standart sapmasını hesapla
        mean_value = np.mean(image_array)

        # Threshold değerini hesapla
        threshold_value = mean_value

        # Resmi threshold değeriyle sınıflandır
        classified = np.where(image_array > threshold_value, 255, 0)

        # Sınıflandırılmış resmi bir PIL görüntüsüne dönüştür
        result = Image.fromarray(classified.astype('uint8'))

        # Sınıflandırılmış fark görüntüsünü görüntüle
        nameToSave = os.path.splitext(os.path.basename(image_path))[0] + ".png"
        # Görüntüyü kaydet
        out_file_path = f'Image/{combination_name}/7.thresholded'

        # print(f'{nameToSave}(threshold): {threshold_value} ')
        #print(f'{threshold_value} ')

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        result.save(f'{out_file_path}/{nameToSave}')
