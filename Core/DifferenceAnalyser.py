from PIL import Image, ImageChops, ImageOps

# İlk görüntüyü aç ve renkliye dönüştür
img1 = Image.open('../Deneme/Image/Before/20230127.png').convert('RGB')

# İkinci görüntüyü aç ve renkliye dönüştür
img2 = Image.open('../Deneme/Image/After/20230209.png').convert('RGB')

# PILLOW fark al
diff = ImageChops.difference(img1, img2)

# Farklılıkları belirginleştirmek için eşik değeri kullan
threshold = 80
mask = diff.point(lambda x: x > threshold and 255)

# Sonuçları görselleştir
mask.show()

# Normalize edilmiş görüntüyü elde etmek için ImageOps.autocontrast() fonksiyonunu kullanabilirsiniz
normalized = ImageOps.autocontrast(ImageChops.subtract(img1, img2))
# Normalize edilmiş görüntüyü göster
normalized.show()

# Renkli görüntüyü elde etmek için Image.merge() fonksiyonunu kullanabilirsiniz
colored = Image.merge('RGB', [img1, img2, ImageChops.subtract(img1, img2)])
# Renkli görüntüyü göster
colored.show()