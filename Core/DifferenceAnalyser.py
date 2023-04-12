from PIL import Image, ImageChops, ImageOps

# ilk görüntü gri
img1 = Image.open('../Deneme/sınıflandırılmış_goruntu.jpg').convert('L')

# ikinci görüntü gri
img2 = Image.open('../Deneme/sınıflandırılmış_goruntu2.jpg').convert('L')

# PILLOW fark al
diff = ImageChops.difference(img1, img2)

# Farklılıkları belirginleştirmek için eşik değeri kullan
threshold = 2
mask = diff.point(lambda x: x > threshold and 255)

# sonuçları görselleştir
mask.show()

# normalized = ImageOps.autocontrast(ImageChops.subtract(img1, img2))
# # normalleştirilmiş görüntüyü göster
# normalized.show()
#
# colored = Image.merge('RGB', [img1, img2, ImageChops.subtract(img1, img2)])
# # renkli görüntüyü göster
# colored.show()


# '1': 1-bit monochrome image
# 'L': 8-bit grayscale image
# 'P': 8-bit palette image
# 'RGB': 24-bit true color image
# 'RGBA': 32-bit true color image with transparency mask
# 'CMYK': 32-bit color separation image
