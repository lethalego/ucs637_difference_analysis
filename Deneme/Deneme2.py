from PIL import Image, ImageChops

# İki görüntüyü yükle
img1 = Image.open('../Deneme/Image/Before/20230127.png').convert('L')
img2 = Image.open('../Deneme/Image/After/20230209.png').convert('L')

# Boyutları eşitle
img1 = img1.resize(img2.size)

# İki görüntü arasındaki farkı hesapla
diff = ImageChops.difference(img2, img1)

# Yoğunluk farkına göre sınıflandır
threshold_value = 60
classified = diff.point(lambda p: 255 if p > threshold_value else 0, '1')

# Sınıflandırılmış fark görüntüsünü görüntüle
classified.show()

classified.save("result2.png")
