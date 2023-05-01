import glob
import os

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
    normalyzer.mormalyze_min_max("before", path)

# 4.2 after
file_paths_after_stacked = file_operations.find_file_under_folder_with_extension("Image/3.stack/after", ".png")
for path in file_paths_after_stacked:
    normalyzer.mormalyze_min_max("after", path)


# 5.	 Enhencement- histogram eşitleme çalıştır kaydet

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
    thresholder.apply_threshold(path, 100)

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

# 9.	 Görüntünün m2 hesapla
# 10.	 Değişim gösterenlerin m2 hesapla
# 11.	 En çok değişim oranlarını bul
# 12.	 Değişim oranıyla nüfusu birleştir
