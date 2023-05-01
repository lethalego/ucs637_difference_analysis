from PIL import Image
from matplotlib import pyplot as plt

# Görüntüyü yükle ve gri seviyeye dönüştür
alimage = Image.open("Output/Deneme9_fark.png").convert("L")

# Piksel sınıflarını oluştur
color_classes = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
class_names = ["Yeşil", "Kırmızı", "Mavi", "Sarı", "Pembe"]
class_colors = {class_names[i]: color_classes[i] for i in range(5)}
pixel_classes = []
for i in range(5):
    pixel_classes.append([])

# Her pikselin sınıfını belirle
pixels = alimage.load()
for y in range(alimage.height):
    for x in range(alimage.width):
        pixel_value = pixels[x, y]
        class_index = int(pixel_value / 51)
        pixel_classes[class_index].append((x, y))

# Sınıflara ait piksel sayısını hesapla ve ekrana yazdır
for i in range(5):
    print("Sınıf", i + 1, "piksel sayısı:", len(pixel_classes[i]))

# Yeni görüntüyü oluştur ve ekrana göster
new_image = Image.new("RGB", (alimage.width, alimage.height))
new_pixels = new_image.load()
for i in range(5):
    for pixel in pixel_classes[i]:
        new_pixels[pixel[0], pixel[1]] = color_classes[i]


for class_name, color in class_colors.items():
    plt.plot([], [], color=color, label=class_name)

plt.legend()
plt.show()
