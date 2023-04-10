import os

import matplotlib.pyplot as plt
import numpy as np
from sentinelhub import CRS, BBox, DataCollection, MimeType, WcsRequest
from sentinelhub import SHConfig

from Config import EnvSetup
from Config.ConfigSetupWCS import ConfigSetupWCS
from Core.ImagePlotter import plot_image

print("Here we go WCS")

envSetup = EnvSetup.EnvSetup()

config = SHConfig()
config.sh_client_id = envSetup.client_Id
config.sh_client_secret = envSetup.client_secret
config.instance_id = envSetup.instance_id

configSetup = ConfigSetupWCS()

wcs_bands_request = WcsRequest(
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

bands_img_temp = wcs_bands_request.get_data(save_data=True)

bands_img_saved = wcs_bands_request.get_data()

bands_img = bands_img_saved

if np.array_equal(bands_img_temp[-1], bands_img_saved[-1]):
    print("Arrays are equal.")

else:
    print("Arrays are different.")
    bands_img = wcs_bands_request.get_data(redownload=True)


for folder, _, filenames in os.walk(wcs_bands_request.data_folder):
    for filename in filenames:
        print(os.path.join(folder, filename))

# plot_image(bands_img[-1])  # 3 bandın karışımı true image vermesi lazım

plot_image(bands_img[-1][:, :, [3]], 2.5 / 255)  # 3
plt.show()

plot_image(bands_img[-1][:, :, [2]], 2.5 / 255)  # 2
plt.show()

plot_image(bands_img[-1][:, :, [1]], 2.5 / 255)  # 1
plt.show()

os.listdir(wcs_bands_request.data_folder)

#
# print(wms_bands_img[-1][:, :, 12].shape)
#
print("These %d images were taken on the following dates:" % len(bands_img))
for index, date in enumerate(wcs_bands_request.get_dates()):
    print(" - image %d was taken on %s" % (index, date))
#
# print("Returned data is of type = %s and length %d." % (type(wms_bands_img), len(wms_bands_img)))
#
# print(
#     "Single element in the list is of type {} and has shape {}".format(
#         type(wms_bands_img[-1]), wms_bands_img[-1].shape
#     )
# )
#
print(
    "Bulut yüzdesi > %1.0f%%."
    % (wcs_bands_request.maxcc * 100.0)
)
