from PIL import Image, ImageChops

# İki görüntüyü yükle
img1 = Image.open('../Deneme/Image/before.png').convert('L')
img2 = Image.open('../Deneme/Image/after.png').convert('L')

# Boyutları eşitle
img1 = img1.resize(img2.size)

# İki görüntü arasındaki farkı hesapla
diff = ImageChops.difference(img2, img1)

# Yoğunluk farkına göre sınıflandır
threshold_value = 100
classified = diff.point(lambda p: 255 if p > threshold_value else 0, '1')

# Sınıflandırılmış fark görüntüsünü görüntüle
classified.show()

classified.save("Output/deneme2_result2_s.png")
