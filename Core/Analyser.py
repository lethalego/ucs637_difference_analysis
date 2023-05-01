import glob
import os

from Core.BandStacker import BandStacker
from Core.DifferenceFinder import DifferenceFinder
from Core.FileOperations import FileOperations
from Core.Masker import Masker
from Core.Normalyzer import Normalyzer
from Core.WCSMapFetcher import WCSMapFetcher

file_operations = FileOperations()

# # 1.	 TIFF olarak indir Image/raw altına yaz
# fetcher = WCSMapFetcher()
# fetcher.get_map("before")
# fetcher.get_map("after")
#
# # 2.	 GeoJson ile parçala ve kaydet Image/masked/before Image/raw/after
# masker = Masker()
#
#
# before_tiff_path = file_operations.find_file_under_folder_with_extension("Image/raw/before", ".tiff")[0]
# after_tiff_path = file_operations.find_file_under_folder_with_extension("Image/raw/after", ".tiff")[0]
#
# # 2.1 before
#
# masker.split_image("before",
#                    before_tiff_path,
#                    "../resources/AdiyamanBolgelerGeo.json")
#
# # 2.2 after
# masker.split_image("after",
#                    after_tiff_path,
#                    "../resources/AdiyamanBolgelerGeo.json")

# # 3.	 4 3 2 bantlarını birleştir kaydet
# bandStacker = BandStacker()
#
# # 3.1 before
# file_paths_before_masked = file_operations.find_file_under_folder_with_extension("Image/masked/before", ".tiff")
# for path in file_paths_before_masked:
#     bandStacker.stack_bands_into_one_true_color_image("before", path)
#
# # 3.2 after
# file_paths_after_masked = file_operations.find_file_under_folder_with_extension("Image/masked/after", ".tiff")
# for path in file_paths_after_masked:
#     bandStacker.stack_bands_into_one_true_color_image("after", path)
#
# # 4.	 Enhencement- k means algorithm çalıştır kaydet
#
# normalyzer = Normalyzer()
#
# # 4.1 before
# file_paths_before_stacked = file_operations.find_file_under_folder_with_extension("Image/stack/before", ".png")
# for path in file_paths_before_stacked:
#     normalyzer.mormalyze_min_max("before", path)
#
# # 4.2 after
# file_paths_after_stacked = file_operations.find_file_under_folder_with_extension("Image/stack/after", ".png")
# for path in file_paths_after_stacked:
#     normalyzer.mormalyze_min_max("after", path)
#
#
# # 5.	 Enhencement- histogram eşitleme çalıştır kaydet
#
# # 5.1 before
# file_paths_before = file_operations.find_file_under_folder_with_extension("Image/normalyzed/before", ".png")
# for path in file_paths_before:
#     normalyzer.normalyze_histogram("before", path)
#
# # 5.2 after
# file_paths_after = file_operations.find_file_under_folder_with_extension("Image/normalyzed/after", ".png")
# for path in file_paths_after:
#     normalyzer.normalyze_histogram("after", path)


# 6.	 Fark al kaydet
difference_finder = DifferenceFinder()

file_paths_before = file_operations.find_file_under_folder_with_extension("Image/histogram/before", ".png")

for path in file_paths_before:
    # Dosya adını almak için os.path.basename() kullanabiliriz
    filename = os.path.basename(path)
    # Aynı dosya adına sahip dosyaları aramak için glob.glob() kullanabiliriz
    matching_files = glob.glob(f"Image/histogram/after/{filename}")
    # Eşleşen dosya varsa, dosya yollarını yazdırabiliriz
    if len(matching_files) > 0:
        difference_finder.get_difference(path, matching_files[0])


# 7.	 Farkı orijinal görüntüye oturt kaydet
# 8.	 Görüntünün m2 hesapla
# 9.	 Değişim gösterenlerin m2 hesapla
# 10.	 En çok değişim oranlarını bul
# 11.	 Değişim oranıyla nüfusu birleştir
