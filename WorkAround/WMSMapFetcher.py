import os

import numpy as np

from Config import EnvSetup
from sentinelhub import SHConfig
from sentinelhub import CRS, BBox, DataCollection, WmsRequest

import matplotlib.pyplot as plt

from Config.ConfigSetupWMS import ConfigSetupWMS
from Core.ImagePlotter import plot_image, plot_image_layout, plot_image_layout2

print("Here we go WMS")

envSetup = EnvSetup.EnvSetup()

config = SHConfig()
config.sh_client_id = envSetup.client_Id
config.sh_client_secret = envSetup.client_secret
config.instance_id = envSetup.instance_id

configSetup = ConfigSetupWMS()

bbox = BBox(bbox=configSetup.coords_wgs84, crs=CRS.WGS84)

xRatio = (configSetup.coords_wgs84[2] - configSetup.coords_wgs84[0])
yRatio = (configSetup.coords_wgs84[1] - configSetup.coords_wgs84[3])

ratio = (configSetup.coords_wgs84[2] - configSetup.coords_wgs84[0]) / (
            configSetup.coords_wgs84[1] - configSetup.coords_wgs84[3])

wms_true_color_request = WmsRequest(
    data_collection=DataCollection.SENTINEL2_L2A,
    layer=configSetup.layer,
    bbox=bbox,
    time=configSetup.time_range,
    width=int(configSetup.image_width * ratio),
    height=configSetup.image_height,
    config=config,
    maxcc=configSetup.cloud_coverage,
    data_folder=configSetup.data_folder
)

bands_img_temp = wms_true_color_request.get_data(save_data=True)

bands_img_saved = wms_true_color_request.get_data()

bands_img = bands_img_saved

if np.array_equal(bands_img_temp[-1], bands_img_saved[-1]):
    print("Arrays are equal.")

else:
    print("Arrays are different.")
    bands_img = wms_true_color_request.get_data(redownload=True)


for folder, _, filenames in os.walk(wms_true_color_request.data_folder):
    for filename in filenames:
        print(os.path.join(folder, filename))

image_brigthness_factor = factor = 1.5 / 255

plot_image(bands_img[-1], factor=image_brigthness_factor)
plt.show()

list1 = []

for index, date in enumerate(wms_true_color_request.get_dates()):
    print(" * Görüntü %d tarihi: %s" % (index, date))
    t = (" * Görüntü %d tarihi: %s" % (index, date))
    list1.append(t)

plot_image_layout2(bands_img, ratio, list1, factor=image_brigthness_factor)
plt.show()

print("Tarih aralığında mevcut Sentinel-2 görüntü sayısı %d" % len(bands_img))
print(
    "Bulut yüzdesi > %1.0f%%."
    % (wms_true_color_request.maxcc * 100.0)
)

print(
    "Görüntü tipi(type): {} ve şekli(shape) {}".format(
        type(bands_img[-1]), bands_img[-1].shape
    )
)
