from PIL import Image, ImageChops
from matplotlib import pyplot as plt

from Core.ImagePlotter import plot_image

# İlk görüntüyü yükle
img1 = Image.open("../Core/test_dir_tiff_2/62fef535a3cc9b2a778c7d22489916aa/response.png")

# İkinci görüntüyü yükle
img2 = Image.open("../Core/test_dir_tiff_2/7761716bf7d8cefd667311864bce69cb/response.png")

# Farklı pikselleri beyaz, aynı pikselleri siyah olarak işaretle
diff = ImageChops.difference(img1, img2).convert('1')

# Değişiklikleri sınıflandırmak için piksellerin RGB değerlerini alın
rgb_im = img1.convert('RGB')
rgb_diff = diff.convert('RGB')

# Değişikliklerin renk sınıflarına atanması
color_classes = {
    (255, 255, 255): "White",
    (255, 0, 0): "Red",
    (255, 255, 0): "Yellow",
    (0, 255, 0): "Green",
    (0, 0, 255): "Blue",
    (0, 0, 0): "Black"
}

for x in range(rgb_diff.width):
    for y in range(rgb_diff.height):
        # Farklı piksellerin RGB değerlerini alın
        diff_r, diff_g, diff_b = rgb_diff.getpixel((x, y))

        # Değişiklik sınıfını belirleyin
        diff_class = color_classes.get((diff_r, diff_g, diff_b), None)

        if diff_class:
            # Değişiklik pikselinin RGB değerlerini alın
            r, g, b = rgb_im.getpixel((x, y))

            # Değişiklik sınıfına göre farklı renklerle işaretle
            if diff_class == "White":
                rgb_im.putpixel((x, y), (255, 255, 255))
            elif diff_class == "Red":
                rgb_im.putpixel((x, y), (255, g, b))
            elif diff_class == "Yellow":
                rgb_im.putpixel((x, y), (255, 255, b))
            elif diff_class == "Green":
                rgb_im.putpixel((x, y), (r, 255, b))
            elif diff_class == "Blue":
                rgb_im.putpixel((x, y), (r, g, 255))
            else:
                rgb_im.putpixel((x, y), (0, 0, 0))

# Sonuç görüntüsünü kaydet
# plot_image(rgb_im, factor=2.5 / 255)
# plt.figure(figsize=(100, 100))
# plt.show()

rgb_im.save("result.png")
