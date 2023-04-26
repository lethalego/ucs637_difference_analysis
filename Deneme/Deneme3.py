from PIL import Image
import cv2
import numpy as np

# İlk görüntüyü yükle
img1 = Image.open('../Deneme/Image/before.png')

# İkinci görüntüyü yükle
img2 = Image.open('../Deneme/Image/after.png')

# Görüntüleri NumPy dizilerine dönüştür
img1_np = np.array(img1)
img2_np = np.array(img2)

# Gri tonlamalı görüntüleri elde et
img1_gray = cv2.cvtColor(img1_np, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2_np, cv2.COLOR_BGR2GRAY)

# Fark görüntüsünü elde et
img_diff = cv2.absdiff(img1_gray, img2_gray)

# Canny kenar tespiti uygula
edges = cv2.Canny(img_diff, 50, 150)

# Sonucu PIL formatında kaydet
result = Image.fromarray(edges)
result.show()