import os

from matplotlib import pyplot as plt
from skimage.metrics import structural_similarity as ssim
from PIL import Image, ImageOps
from sklearn.metrics import confusion_matrix

import numpy as np
import seaborn as sns


class AccourcyFinder:

    def find_accourcy(self, file_path, combination_name):
        image = Image.open(f'{file_path}/#PL_Test.png')
        # Diziyi dönüştürme ve veri tipini ayarlama
        image_array = np.array(image, dtype=np.uint8)
        if (image_array.max() == 1):
            image_array = image_array * 255

        image_test_array = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 255, 255, 0, 0, 0, 0, 0, 0, 0],
            [0, 255, 255, 0, 0, 0, 0, 0, 0, 0],
            [0, 255, 255, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 255, 255, 0, 0],
            [255, 255, 0, 0, 0, 255, 255, 255, 0, 0],
            [255, 0, 0, 0, 0, 255, 255, 255, 0, 0],
            [0, 0, 0, 0, 0, 255, 255, 0, 0, 0]
        ])

        # Diziyi resme dönüştürme
        imtest = Image.fromarray(image_test_array.astype(np.uint8), mode='L')

        # Doğruluk analizi
        match_count = 0
        total_pixels = image_array.shape[0] * image_array.shape[1]

        for i in range(image_array.shape[0]):
            for j in range(image_array.shape[1]):
                if image_array[i, j] == image_test_array[i, j]:
                    match_count += 1

        accuracy = (match_count / total_pixels) * 100

        # Sonuçları yazdırma
        # print("Eşleşen piksel sayısı:", match_count)
        # print("Doğruluk oranı (%):", accuracy)

        # dogruluk = np.mean(image_array == image_test_array)
        #
        # print("Doğruluk:", dogruluk)

        # # MSE hesaplama
        # mse = np.mean((image_array - image_test_array) ** 2)
        #
        # # Normalizasyon
        # normalized_mse = (mse / (255 ** 2)) * 100
        #
        # print("Normalized MSE:", normalized_mse)
        #
        # # SSIM hesaplama
        # ssim_degeri = ssim(image_array, image_test_array, data_range=image_array.max() - image_array.min())
        #
        # print("SSIM Değeri:", ssim_degeri)
        ##################################################################
        # Doğru eşleşen piksellerin sayısını bulma
        dogru_eslesen_pikseller = np.sum(image_array == image_test_array)

        # Toplam piksel sayısı
        toplam_piksel_sayisi = image_array.size

        # Piksel bazında doğruluk oranı
        dogruluk_orani = dogru_eslesen_pikseller / toplam_piksel_sayisi

        # print("Piksel Bazında Doğruluk Oranı:", dogruluk_orani)

        #########################################################
        # Doğruluk matrisini oluşturma
        confusion_mat = confusion_matrix(image_test_array.flatten(), image_array.flatten())

        TP = confusion_mat[1, 1]  # Gerçek pozitif sayısı
        TN = confusion_mat[0, 0]  # Gerçek negatif sayısı
        FP = confusion_mat[0, 1]  # Yanlış pozitif sayısı
        FN = confusion_mat[1, 0]  # Yanlış negatif sayısı

        print(TP)
        print(TN)
        print(FP)
        print(FN)

        # print("Confusion Matrix:")
        print(confusion_mat)

        # Doğruluk oranı hesaplama
        acc = self.accuracy(confusion_mat)
        print(acc)

        # Hassasiyet hesaplama
        prec = self.precision(confusion_mat)
        print(prec)

        # Özgünlük hesaplama
        spec = self.specificity(confusion_mat)
        print(spec)

        # Duyarlılık hesaplama
        rec = self.recall(confusion_mat)
        print(rec)

        # F1 skoru hesaplama
        f1 = self.f1_score(confusion_mat)
        print(f1)

        plt.clf()
        # Karışıklık matrisini görselleştirme
        sns.heatmap(confusion_mat, annot=True, cmap='Blues', fmt='d')
        plt.xlabel("Tahmin Edilen Etiket")
        plt.ylabel("Gerçek Etiket")
        plt.title(f"Karışıklık Matrisi({combination_name})")

        name_to_save = "confusionMatix.png"
        # Görüntüyü kaydet
        out_file_path = f'Image/{combination_name}/8.result'

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        plt.savefig(f'{out_file_path}/plot_{combination_name}{name_to_save}')

        plt.clf()

        # Doğruluk, hassasiyet, özgünlük, duyarlılık ve F1 skoru görselleştirme
        metrics = ['Doğruluk', 'Hassasiyet', 'Özgünlük', 'Duyarlılık', 'F1 Skoru']
        values = [acc, prec, spec, rec, f1]

        plt.bar(metrics, values)
        plt.xlabel("Metrik")
        plt.ylabel("Değer")
        plt.title(f"Performans Metrikleri({combination_name})")

        name_to_save = "performance.png"
        # Görüntüyü kaydet
        out_file_path = f'Image/{combination_name}/8.result'

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        plt.savefig(f'{out_file_path}/plot_{combination_name}{name_to_save}')

    def accuracy(self, confusion_matrix):
        tp = confusion_matrix[1, 1]
        tn = confusion_matrix[0, 0]
        fp = confusion_matrix[0, 1]
        fn = confusion_matrix[1, 0]

        total = tp + tn + fp + fn
        accuracy_score = (tp + tn) / total
        return accuracy_score

    def precision(self, confusion_matrix):
        tp = confusion_matrix[1, 1]
        fp = confusion_matrix[0, 1]

        if ((tp + fp) == 0):
            precision_score = 0
        else:
            precision_score = tp / (tp + fp)
        return precision_score

    def specificity(self, confusion_matrix):
        tn = confusion_matrix[0, 0]
        fp = confusion_matrix[0, 1]

        specificity_score = tn / (tn + fp)
        return specificity_score

    def recall(self, confusion_matrix):
        tp = confusion_matrix[1, 1]
        fn = confusion_matrix[1, 0]

        recall_score = tp / (tp + fn)
        return recall_score

    def f1_score(self, confusion_matrix):
        precision_score = self.precision(confusion_matrix)
        recall_score = self.recall(confusion_matrix)

        if ((precision_score + recall_score) == 0):
            f1_score = 0
        else:
            f1_score = 2 * (precision_score * recall_score) / (precision_score + recall_score)

        return f1_score
