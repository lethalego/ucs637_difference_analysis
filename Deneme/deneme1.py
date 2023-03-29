import os

import numpy as np
import rasterio
from jinja2 import meta
from matplotlib import pyplot as plt
from matplotlib.pyplot import show
from sentinelhub import WcsRequest, BBox, CRS, DataCollection, MimeType, SHConfig
from skimage import io

from Config import EnvSetup
from Config.ConfigSetup import ConfigSetup

# Sentinel Hub hesap bilgileri
envSetup = EnvSetup.EnvSetup()

config = SHConfig()
config.sh_client_id = envSetup.client_Id
config.sh_client_secret = envSetup.client_secret
config.instance_id = envSetup.instance_id

configSetup = ConfigSetup()

# Tarih aralığı
time_interval = ('2023-02-01', '2023-02-28')

# WCS isteği
wcs_request = WcsRequest(
    data_collection=DataCollection.SENTINEL2_L2A,
    layer='ALL_BANDS',
    bbox=BBox(bbox=configSetup.coords_wgs84_WCS, crs=CRS.WGS84),
    time=time_interval,
    image_format=MimeType.TIFF,
    resx='10m',
    resy='10m',
    maxcc=0.2,  # Bulut örtüsü oranı
    config=config,
    data_folder='deneme_tiff'
)

data_temp = wcs_request.get_data(save_data=True)

data_saved = wcs_request.get_data()

data = data_saved

if np.array_equal(data_temp[-1], data_saved[-1]):
    print("Arrays are equal.")

else:
    print("Arrays are different.")
    data = wcs_request.get_data(redownload=True)

for folder, _, filenames in os.walk(wcs_request.data_folder):
    for filename in filenames:
        print(os.path.join(folder, filename))

# # Yeni dosya adı ve dosya modu tanımlama
# new_file_name = 'new_image.tif'
# file_mode = 'w'
#
# # Dosyanın açılması ve verilerin yazılması
# with rasterio.open(new_file_name, file_mode, **meta) as dst:
#     dst.write(data)

# Kaydedilen görüntüyü getirme ve gösterme
with rasterio.open('deneme_tiff/1d4a5bde06b55e59838e4d68e04512b4/response.tiff') as src:
    print('Width:', src.width)
    print('Height:', src.height)
    print('Number of bands:', src.count)

    # Raster hakkında metadata bilgilerine erişebiliriz
    print('Metadata:', src.meta)

    # Raster verisini yükleyebiliriz
    # raster = src.read(1)  # ilk bant
    img = src.read(1)
    plt.imshow(img)
    plt.show()

bands = ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B8A', 'B09', 'B11', 'B12']

# Kaydedilen görüntünün bütün bantlarını layout olarak gösterme
fig, axs = plt.subplots(3, 4, figsize=(12, 9))
for i, band in enumerate(bands):
    with rasterio.open('deneme_tiff/1d4a5bde06b55e59838e4d68e04512b4/response.tiff') as src:
        img = src.read(i + 1)
        axs[i // 4, i % 4].imshow(img)
        axs[i // 4, i % 4].set_title(band)
plt.tight_layout()
plt.show()

# NDVI analizi yapma ve gösterme
RED_BAND = 4
NIR_BAND = 8

with rasterio.open('deneme_tiff/1d4a5bde06b55e59838e4d68e04512b4/response.tiff') as dataset:
    red = dataset.read(RED_BAND)
with rasterio.open('deneme_tiff/1d4a5bde06b55e59838e4d68e04512b4/response.tiff') as dataset:
    nir = dataset.read(NIR_BAND)

np.seterr(divide='ignore', invalid='ignore')
ndvi = np.true_divide(nir - red, nir + red)
ndvi[ndvi == np.inf] = 0
ndvi = np.nan_to_num(ndvi)

# NDVI grafiği 1
plt.figure(figsize=(8, 8))
im = plt.imshow(ndvi, cmap='RdYlGn', vmin=-1, vmax=1)
plt.title('Normalized Difference Vegetation Index (NDVI) Map')
plt.xlabel('Column Pixels')  # x eksen etiketi
plt.ylabel('Row Pixels')  # y eksen etiketi
cbar = plt.colorbar(im, fraction=0.045, pad=0.04, format='%.2f')
cbar.ax.set_ylabel('NDVI Value')
plt.show()

