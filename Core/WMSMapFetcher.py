import numpy as np
import slots as slots

from Config import EnvSetup
from sentinelhub import SHConfig
from sentinelhub import CRS, BBox, DataCollection, WmsRequest

import matplotlib.pyplot as plt

from Config.ConfigSetup import ConfigSetup
from Core.ImagePlotter import plot_image

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

plot_image(wms_true_color_img[-1], factor=3.5 / 255)
plt.show()



# some stuff for pretty plots
ncols = 4
nrows = 3
aspect_ratio = configSetup.coords_wgs84[0] / configSetup.coords_wgs84[1]
subplot_kw = {"xticks": [], "yticks": [], "frame_on": False}

fig, axs = plt.subplots(ncols=ncols, nrows=nrows, figsize=(5 * ncols * aspect_ratio, 5 * nrows), subplot_kw=subplot_kw)

for idx, image in enumerate(wms_true_color_img):
    ax = axs[idx // ncols][idx % ncols]
    ax.imshow(np.clip(image * 2.5 / 255, 0, 1))
    ax.set_title(f"{idx}", fontsize=10)

plt.tight_layout()
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
