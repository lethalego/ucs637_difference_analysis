import glob
import os

from skimage.metrics import structural_similarity as ssim
from PIL import Image, ImageOps
import numpy as np

from Core.BandStacker import BandStacker
from Core.DifferenceFinder import DifferenceFinder
from Core.FileOperations import FileOperations
from Core.Masker import Masker
from Core.Normalyzer import Normalyzer
from Core.ResultPlotter import ResultPlotter
from Core.Thresholder import Thresholder
from Core.WCSMapFetcher import WCSMapFetcher

file_operations = FileOperations()

# 1.	 TIFF olarak indir Image/raw altına yaz
fetcher = WCSMapFetcher()
fetcher.get_map("before")
fetcher.get_map("after")

# 2.	 GeoJson ile parçala ve kaydet Image/masked/before Image/raw/after
masker = Masker()

before_tiff_path = file_operations.find_file_under_folder_with_extension("Image/1.raw/before", ".tiff")[0]
after_tiff_path = file_operations.find_file_under_folder_with_extension("Image/1.raw/after", ".tiff")[0]

# 2.1 before

masker.split_image("before",
                   before_tiff_path,
                   "../resources/AdiyamanBolgelerGeo.json")

# 2.2 after
masker.split_image("after",
                   after_tiff_path,
                   "../resources/AdiyamanBolgelerGeo.json")

# 3. 4 3 2 bantlarını birleştir kaydet
bandStacker = BandStacker()

# 3.1 before
file_paths_before_masked = file_operations.find_file_under_folder_with_extension("Image/2.masked/before", ".tiff")
for path in file_paths_before_masked:
    bandStacker.stack_bands_into_one_true_color_image("before", path)

# 3.2 after
file_paths_after_masked = file_operations.find_file_under_folder_with_extension("Image/2.masked/after", ".tiff")
for path in file_paths_after_masked:
    bandStacker.stack_bands_into_one_true_color_image("after", path)

# 4. Enhencement- k means algorithm çalıştır kaydet

normalyzer = Normalyzer()

# 4.1 before
file_paths_before_stacked = file_operations.find_file_under_folder_with_extension("Image/3.stack/before", ".png")
for path in file_paths_before_stacked:
    normalyzer.normalize_clahe("before", path)

# 4.2 after
file_paths_after_stacked = file_operations.find_file_under_folder_with_extension("Image/3.stack/after", ".png")
for path in file_paths_after_stacked:
    normalyzer.normalize_clahe("after", path)

# 5.	 Enhancement- histogram eşitleme çalıştır kaydet

# 5.1 before
file_paths_before = file_operations.find_file_under_folder_with_extension("Image/4.normalyzed/before", ".png")
for path in file_paths_before:
    normalyzer.normalyze_histogram("before", path)

# 5.2 after
file_paths_after = file_operations.find_file_under_folder_with_extension("Image/4.normalyzed/after", ".png")
for path in file_paths_after:
    normalyzer.normalyze_histogram("after", path)

# 6.	 Fark al kaydet
difference_finder = DifferenceFinder()

file_paths_before = file_operations.find_file_under_folder_with_extension("Image/5.histogram/before", ".png")

for path in file_paths_before:
    # Dosya adını almak için os.path.basename() kullanabiliriz
    filename = os.path.basename(path)
    # Aynı dosya adına sahip dosyaları aramak için glob.glob() kullanabiliriz
    matching_files = glob.glob(f"Image/5.histogram/after/{filename}")
    # Eşleşen dosya varsa, dosya yollarını yazdırabiliriz
    if len(matching_files) > 0:
        difference_finder.get_difference(path, matching_files[0])

# 7. threshold uygula

thresholder = Thresholder()
file_paths_difference = file_operations.find_file_under_folder_with_extension("Image/6.difference", ".png")
for path in file_paths_difference:
    # thresholder.apply_threshold(path, 55)
    # thresholder.apply_mean_threshold(path) #14.4
    #thresholder.apply_threshold_otsu(path)  # ortalama eşik değer 65.8, 255 ler olmayınca 44.78
    thresholder.apply_threshold_gaussian(path) #ortalama eşik değer 56.8

# 8.	 Farkı orijinal görüntüye oturt kaydet
result_plotter = ResultPlotter()

file_paths_before = file_operations.find_file_under_folder_with_extension("Image/3.stack/before", ".png")

for path in file_paths_before:
    # Dosya adını almak için os.path.basename() kullan
    filename = os.path.basename(path)
    # Aynı dosya adına sahip dosyaları aramak için glob.glob() kullan
    matching_files_after = glob.glob(f"Image/3.stack/after/{filename}")
    matching_files_difference_thresholded = glob.glob(f"Image/7.thresholded/{filename}")
    # Eşleşen dosya varsa, dosya yollarını yazdırabiliriz
    if len(matching_files_after) > 0:
        result_plotter.aplly_plot(path, matching_files_after[0], matching_files_difference_thresholded[0])

image = Image.open(f'../Core/Image/7.thresholded/#PL_Test.png')
# Diziyi dönüştürme ve veri tipini ayarlama
image_array = np.array(image, dtype=np.uint8)

# Dizideki True ve False değerlerini 0 ve 255 olarak değiştirme
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
print("Eşleşen piksel sayısı:", match_count)
print("Doğruluk oranı (%):", accuracy)

dogruluk = np.mean(image_array == image_test_array)

print("Doğruluk:", dogruluk)

# MSE hesaplama
mse = np.mean((image_array - image_test_array) ** 2)

# Normalizasyon
normalized_mse = (mse / (255 ** 2)) * 100

print("Normalized MSE:", normalized_mse)

# SSIM hesaplama
ssim_degeri = ssim(image_array, image_test_array, data_range=image_array.max() - image_array.min())

print("SSIM Değeri:", ssim_degeri)
##################################################################
# Doğru eşleşen piksellerin sayısını bulma
dogru_eslesen_pikseller = np.sum(image_array == image_test_array)

# Toplam piksel sayısı
toplam_piksel_sayisi = image_array.size

# Piksel bazında doğruluk oranı
dogruluk_orani = dogru_eslesen_pikseller / toplam_piksel_sayisi

print("Piksel Bazında Doğruluk Oranı:", dogruluk_orani)

#########################################################
# Doğruluk matrisini oluşturma
dogruluk_matrisi = image_array == image_test_array

print("Doğruluk Matrisi:")
print(dogruluk_matrisi)
