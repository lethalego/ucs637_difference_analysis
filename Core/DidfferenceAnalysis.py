from PIL import Image, ImageChops

# ilk görüntüyü yükle
img1 = Image.open('test_dir_tiff_2/4d9c97ddb6fc640d1b46a8950aa0f234/response.png').convert('L')

# ikinci görüntüyü yükle
img2 = Image.open('test_dir_tiff_2/8d487696a3097c003134b93c01cb9856/response.png').convert('L')

# fark analizini yapmak için görüntülerin farkını al
diff = ImageChops.difference(img1, img2)

# farklılıkları belirginleştirmek için eşik değeri kullan
threshold = 50
mask = diff.point(lambda x: x > threshold and 255)

# sonuçları görselleştir
mask.show()
