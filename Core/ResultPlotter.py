import os

import numpy as np
from PIL import Image, ImageEnhance
from matplotlib import pyplot as plt


class ResultPlotter:

    def aplly_plot(self, before_path, after_path, diff_path, combination_name):
        # İki görüntüyü yükleme
        img1 = Image.open(f'{before_path}')
        img2 = Image.open(f'{after_path}')
        diff = Image.open(f'{diff_path}')

        # Parlaklığı artırmak için ImageEnhance.Brightness() yöntemini kullanma
        brightness_converter = ImageEnhance.Brightness(img1)
        img1 = brightness_converter.enhance(1.5)  # Değeri artırarak parlaklığı artır

        brightness_converter = ImageEnhance.Brightness(img2)
        img2 = brightness_converter.enhance(1.5)  # Değeri artırarak parlaklığı artır

        # Fark görüntüsünden kırmızı pikselleri belirleme
        diff_array = np.array(diff)
        red_pixels = np.where(diff_array > 0)

        # Kırmızı pikselleri belirtilen renkte gösterme
        result = img1.copy()
        pixels = result.load()
        for x, y in zip(red_pixels[1], red_pixels[0]):
            pixels[x, y] = (255, 0, 0)

        # Piksel sayılarını hesaplama

        img_array = np.array(img1)
        black_pixels = np.where((img_array[:, :, 0] == 0) & (img_array[:, :, 1] == 0) & (img_array[:, :, 2] == 0))
        black_pixels_count = len(black_pixels[0])

        total_pixels = (img1.width * img1.height) - black_pixels_count
        red_pixel_count = len(red_pixels[0])

        # X ve Y eksenlerinin uzunluğunu hesapla
        x_length = img1.width * 10
        y_length = img1.height * 10

        # 2*2 lik plot oluştur
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
        fig.suptitle('Görüntüler')

        ax1.imshow(img1, extent=[0, x_length, y_length, 0])
        ax1.set_title(f"Önce")
        ax1.set_xlabel("(metre)")

        ax2.imshow(img2, extent=[0, x_length, y_length, 0])
        ax2.set_title(f"Sonra")

        ax3.imshow(diff, extent=[0, x_length, y_length, 0])
        ax3.set_title(f"Toplam piksel sayısı: {total_pixels}")

        ax4.imshow(result, extent=[0, x_length, y_length, 0])
        ax4.set_title(f"Değişen piksel sayısı: {red_pixel_count}")

        fig.subplots_adjust(hspace=0.5, wspace=0.5)

        name_to_save = os.path.splitext(os.path.basename(before_path))[0] + ".png"
        # Görüntüyü kaydet
        out_file_path = f'Image/{combination_name}/8.result'

        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)

        result.save(f'{out_file_path}/{name_to_save}')
        plt.savefig(f'{out_file_path}/plot_{name_to_save}')
