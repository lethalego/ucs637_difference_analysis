import os

import matplotlib.pyplot as plt
import numpy as np
from sentinelhub import CRS, BBox, DataCollection, MimeType, WcsRequest
from sentinelhub import SHConfig

from Config import EnvSetup
from Config.ConfigSetup import ConfigSetup
from Core.ImagePlotter import plot_image

print("Here we go WCS")

envSetup = EnvSetup.EnvSetup()

config = SHConfig()
config.sh_client_id = envSetup.client_Id
config.sh_client_secret = envSetup.client_secret
config.instance_id = envSetup.instance_id

configSetup = ConfigSetup()

wms_bands_request = WcsRequest(
    time=configSetup.time_range,
    config=config,
    maxcc=configSetup.cloud_coverage,
    data_collection=DataCollection.SENTINEL2_L2A,
    layer=configSetup.layer,
    bbox=BBox(bbox=configSetup.coords_wgs84_WCS, crs=CRS.WGS84),
    image_format=MimeType.TIFF,
    data_folder=configSetup.data_folder,
    resx=configSetup.resX,
    resy=configSetup.resY,
)

wms_bands_img_temp = wms_bands_request.get_data(save_data=True)

wms_bands_img_saved = wms_bands_request.get_data()

wms_bands_img = wms_bands_img_saved

if np.array_equal(wms_bands_img_temp[-1], wms_bands_img_saved[-1]):
    print("Arrays are equal.")

else:
    print("Arrays are different.")
    wms_bands_img = wms_bands_request.get_data(redownload=True)


for folder, _, filenames in os.walk(wms_bands_request.data_folder):
    for filename in filenames:
        print(os.path.join(folder, filename))

# plot_image(wms_bands_img[-1])  # 3 bandın karışımı true image vermesi lazım
plot_image(wms_bands_img[-1][:, :, [3]], 2.5/255)  # 3 bandın karışımı true image vermesi lazım
plt.show()

plot_image(wms_bands_img[-1][:, :, [2]], 2.5/255)  # 3 bandın karışımı true image vermesi lazım
plt.show()

plot_image(wms_bands_img[-1][:, :, [1]], 2.5/255)  # 3 bandın karışımı true image vermesi lazım

plt.show()

os.listdir(wms_bands_request.data_folder)

#
# print(wms_bands_img[-1][:, :, 12].shape)
#
# print("There are %d Sentinel-2 images available for date range." % len(wms_bands_img))
#
# print("These %d images were taken on the following dates:" % len(wms_bands_img))
# for index, date in enumerate(wms_bands_request.get_dates()):
#     print(" - image %d was taken on %s" % (index, date))
#
# print("Returned data is of type = %s and length %d." % (type(wms_bands_img), len(wms_bands_img)))
#
# print(
#     "Single element in the list is of type {} and has shape {}".format(
#         type(wms_bands_img[-1]), wms_bands_img[-1].shape
#     )
# )
#
# print(
#     "There are %d Sentinel-2 images available for December 2017 with cloud coverage less than %1.0f%%."
#     % (len(wms_bands_img), wms_bands_request.maxcc * 100.0)
# )
