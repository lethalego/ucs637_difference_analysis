import numpy as np
from PIL import Image, ImageOps, ImageChops

# İlk görüntüyü yükle
im1 = Image.open("../Deneme/Image/before.png")
im1_arr = np.array(im1)

# Ortalamayı ve standart sapmayı hesapla
mean = np.mean(im1_arr)
std = np.std(im1_arr)

# Z skor ile normalleştir
im1_zscores = (im1_arr - mean) / std


# Z-skorları kullanarak görüntüyü normalleştir
im1_norm = (im1_zscores * np.std(im1_arr)) + np.mean(im1_arr)

# Normalleştirilmiş görüntüyü kaydet
Image.fromarray(im1_norm.astype(np.uint8)).save("Output/Deneme10_before_norm.png")

im1_normal = Image.open("Output/Deneme10_before_norm.png")


# İki görüntü arasındaki farkı al
diff = ImageChops.difference(im1, im1_normal)


diff.save("Output/Deneme10_fark.png")


