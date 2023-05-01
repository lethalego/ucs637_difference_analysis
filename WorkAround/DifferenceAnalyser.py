from PIL import Image, ImageChops, ImageOps

# İlk görüntüyü aç ve renkliye dönüştür
img1 = Image.open('Image/before.png').convert('RGB')

# İkinci görüntüyü aç ve renkliye dönüştür
img2 = Image.open('Image/after.png').convert('RGB')

# PILLOW fark al
diff = ImageChops.difference(img1, img2)

# Farklılıkları belirginleştirmek için eşik değeri kullan
threshold = 120
mask = diff.point(lambda x: x > threshold and 255)

# Sonuçları görselleştir
mask.show()

# Normalize edilmiş görüntüyü elde etmek için ImageOps.autocontrast() fonksiyonunu kullanabilirsiniz
normalized = ImageOps.autocontrast(ImageChops.subtract(img1, img2))
# Normalize edilmiş görüntüyü göster
normalized.show()

# Renkli görüntüyü elde etmek için Image.merge() fonksiyonunu kullanabilirsiniz
# Convert the grayscale difference image to RGB mode using ImageOps.colorize()
gray_diff = ImageOps.grayscale(ImageChops.difference(img1, img2))
gray_diff_rgb = gray_diff.convert("RGB")

# Merge the RGB images with the colorized grayscale difference image
colored = Image.merge('RGB', [img1, img2, gray_diff_rgb])
# Renkli görüntüyü göster
colored.show()