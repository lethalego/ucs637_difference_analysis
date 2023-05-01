import numpy as np
import rasterio
from matplotlib import pyplot as plt

from Core.ImagePlotter import plot_image

imagePath = '../Deneme/Image/before.tiff'

# Kaydedilen görüntüyü getir
with rasterio.open(imagePath) as src:
    print('Width:', src.width)
    print('Height:', src.height)
    print('Number of bands:', src.count)

    # Raster hakkında metadata bilgilerine erişebiliriz
    print('Metadata:', src.meta)

    # Raster verisini yükleyebiliriz
    # raster = src.read(1)  # ilk bant
    # img = src.read(1)
    # plt.imshow(img)
    # plt.title = 'B01'
    # plt.show()

bands = ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B8A', 'B09', 'B11', 'B12']

# Kaydedilen görüntünün bütün bantlarını layout olarak göster
fig, axs = plt.subplots(3, 4, figsize=(12, 9))
for i, band in enumerate(bands):
    with rasterio.open(imagePath) as src:
        img = src.read(i + 1)
        axs[i // 4, i % 4].imshow(img)
        axs[i // 4, i % 4].set_title(band)
plt.tight_layout()
plt.show()

# NDVI analizi yapma ve gösterme


BLUE_BAND = 2
GREEN_BAND = 3
RED_BAND = 4
NIR_BAND = 8

with rasterio.open(imagePath) as dataset:
    red = dataset.read(RED_BAND)
    nir = dataset.read(NIR_BAND)
    green = dataset.read(GREEN_BAND)
    blue = dataset.read(BLUE_BAND)

# 4 3 2 bandı birleşince true color verir
rgb = np.dstack((red, green, blue))

# parlaklığı artır
plot_image(rgb, factor=2.5 / 255)
plt.show()

np.seterr(divide='ignore', invalid='ignore')
ndvi = np.true_divide(nir - red, nir + red)
ndvi[ndvi == np.inf] = 0
ndvi = np.nan_to_num(ndvi)

# NDVI grafiği 1
plt.figure(figsize=(8, 8))
im = plt.imshow(ndvi, cmap='RdYlGn', vmin=-1, vmax=1)

plt.xlabel('Column Pixels')  # x eksen etiketi
plt.ylabel('Row Pixels')  # y eksen etiketi
cbar = plt.colorbar(im, fraction=0.045, pad=0.04, format='%.2f')
cbar.ax.set_ylabel('NDVI Value')
plt.title = 'Normalized Difference Vegetation Index (NDVI) Map'

plt.show()
