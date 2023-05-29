import numpy as np
from PIL import Image

# Resmi yükle ve gri tonlamaya dönüştür
image = Image.open("Output/Deneme9_fark.png").convert('L')

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
classified_image = Image.fromarray(classified.astype('uint8'))

# Görüntüyü kaydet
classified_image.save("Output/8.png")




