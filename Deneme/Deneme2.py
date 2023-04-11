from PIL import Image, ImageChops

# İki görüntüyü yükle
img1 = Image.open('../Core/test_dir_tiff_2/dee4c3f51ae0caf09409308258ca66ed/response.png').convert('L')
img2 = Image.open('../Core/test_dir_tiff_2/97c5513545feaaa43e95a5be6feee248/response.png').convert('L')

# Boyutları eşitle
img1 = img1.resize(img2.size)

# İki görüntü arasındaki farkı hesapla
diff = ImageChops.subtract(img2, img1)

# Yoğunluk farkına göre sınıflandır
threshold_value = 10
classified = diff.point(lambda p: 255 if p > threshold_value else 0, '1')

# Sınıflandırılmış fark görüntüsünü görüntüle
classified.show()