import numpy as np
from PIL import Image, ImageOps

# İlk görüntüyü yükle
im1 = Image.open("../Deneme/Image/before.png")
im1_arr = np.array(im1)

# İkinci görüntüyü yükle
im2 = Image.open("../Deneme/Image/after.png")
im2_arr = np.array(im2)

# Her iki görüntünün piksel değerleri için z-skor hesapla
im1_zscores = (im1_arr - np.mean(im1_arr)) / np.std(im1_arr)
im2_zscores = (im2_arr - np.mean(im2_arr)) / np.std(im2_arr)

# Z-skorlarını kullanarak her iki görüntüyü normalleştir
im1_norm = (im1_zscores * np.std(im1_arr)) + np.mean(im1_arr)
im2_norm = (im2_zscores * np.std(im2_arr)) + np.mean(im2_arr)

# Normalleştirilmiş görüntüleri kaydet
Image.fromarray(im1_norm.astype(np.uint8)).save("Output/Deneme8_norm_before.png")
Image.fromarray(im2_norm.astype(np.uint8)).save("Output/Deneme8_norm_after.png")


# gri tonlama dönüştürme
img1 = im1.convert('L')
img2 = im2.convert('L')

# float veri tipine dönüştürme ve ortalama ve standart sapma hesaplama
img1 = np.array(img1).astype(np.float32)
img2 = np.array(img2).astype(np.float32)

mean1 = np.mean(img1)
mean2 = np.mean(img2)

std1 = np.std(img1)
std2 = np.std(img2)

# zskor hesaplama
img1_zscore = (img1 - mean1) / std1
img2_zscore = (img2 - mean2) / std2

# 0-255 aralığına ölçeklendirme
img1_norm = (img1_zscore - np.min(img1_zscore)) / (np.max(img1_zscore) - np.min(img1_zscore)) * 255.0
img2_norm = (img2_zscore - np.min(img2_zscore)) / (np.max(img2_zscore) - np.min(img2_zscore)) * 255.0

# iki normalleştirilmiş görüntü arasındaki farkı hesaplama
diff = img1_norm - img2_norm


# eşik değeri belirleme
threshold = 200

# fark görüntüsünde eşik değerinden büyük pikselleri seçme
diff_thresholded = np.where(diff > threshold, diff, 0)

# farklılık olan yerlere eşik değeri uygulandıktan sonra görüntüyü gösterme
Image.fromarray(diff_thresholded.astype('uint8')).show()

# Resimleri yükle


# Resimleri numpy dizisine dönüştür
arr1 = np.array(img1)
arr2 = np.array(img2)

# Farkı hesapla
diff = arr1 - arr2

# Histogram eşitleme
diff_eq = Image.fromarray(diff).convert('L')
diff_eq = ImageOps.equalize(diff_eq)

# Görüntüyü kaydet
diff_eq.save("Output/Deneme8_Fark_Esitlenmis.png")

