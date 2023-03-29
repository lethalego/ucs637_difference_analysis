import numpy as np

from Config import EnvSetup
from sentinelhub import SHConfig
from sentinelhub import CRS, BBox, DataCollection, WmsRequest

import matplotlib.pyplot as plt

from Config.ConfigSetup import ConfigSetup
from Core.ImagePlotter import plot_image, plot_image_layout

print("Here we go WMS")

envSetup = EnvSetup.EnvSetup()

config = SHConfig()
config.sh_client_id = envSetup.client_Id
config.sh_client_secret = envSetup.client_secret
config.instance_id = envSetup.instance_id

configSetup = ConfigSetup()

bbox = BBox(bbox=configSetup.coords_wgs84, crs=CRS.WGS84)

wms_true_color_request = WmsRequest(
    data_collection=DataCollection.SENTINEL2_L2A,
    layer=configSetup.layer,
    bbox=bbox,
    time=configSetup.time_range,
    width=configSetup.image_width,
    height=configSetup.image_height,
    config=config,
    maxcc=configSetup.cloud_coverage
)

wms_true_color_img = wms_true_color_request.get_data() #numpy arrays tipinde resim listesi döner

image_brigthness_factor = factor=1.5 / 255


plot_image(wms_true_color_img[-1], factor=image_brigthness_factor)
plt.show()

plot_image_layout(wms_true_color_img, configSetup.coords_wgs84[0] / configSetup.coords_wgs84[1], factor=image_brigthness_factor)
plt.show()


#
# print("Tarih aralığında mevcut Sentinel-2 görüntü sayısı %d" % len(wms_true_color_img))
# print(
#     "Bulut yüzdesi > %1.0f%%."
#     % (wms_true_color_request.maxcc * 100.0)
# )
#
# print("%d Görüntünün çekildiği tarih:" % len(wms_true_color_img))
#
# for index, date in enumerate(wms_true_color_request.get_dates()):
#     print(" * Görüntü %d tarihi: %s" % (index, date))
#
# print(
#     "Görüntü tipi(type): {} ve şekli(shape) {}".format(
#         type(wms_true_color_img[-1]), wms_true_color_img[-1].shape
#     )
# )
