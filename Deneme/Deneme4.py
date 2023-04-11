import numpy as np
from PIL import Image, ImageChops
import matplotlib.pyplot as plt

# İlk görüntüyü yükle
img1 = Image.open("../Deneme/Image/Before/20230127.png")

# İkinci görüntüyü yükle
img2 = Image.open("../Deneme/Image/After/20230209.png")

# Fark görüntüsünü oluştur
diff = ImageChops.subtract(img1, img2)

# Fark görüntüsünü RGB renk uzayına dönüştür
diff_rgb = diff.convert("RGB")

# Her pikselin normalize edilmiş RGB değerlerini hesapla
def normalize(arr):
    norm = np.linalg.norm(arr)
    if norm == 0:
        return arr
    return np.clip(arr / norm, 0, 255)

diff_rgb_arr = np.asarray(diff_rgb).astype(np.float32)
diff_norm = np.apply_along_axis(normalize, 2, diff_rgb_arr)

# Değişim vektörlerini hesapla
vec_field = diff_norm[:, :, 1] - diff_norm[:, :, 0]

# Diff_norm boyutlarını yeniden boyutlandır
diff_norm_resized = np.resize(diff_norm, vec_field.shape + (3,))

# Quiver plot oluştur
try:
    plt.quiver(vec_field[:, :-1], -vec_field[:-1, :], color=diff_norm_resized[:-1, :-1, :]/255)
    plt.gca().invert_yaxis()
    plt.show()
except ValueError as e:
    print(f"Quiver plot çizdirilemedi: {e}")