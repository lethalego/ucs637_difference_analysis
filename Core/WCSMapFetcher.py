import os

import numpy as np
from sentinelhub import CRS, BBox, DataCollection, MimeType, WcsRequest
from sentinelhub import SHConfig

from Config import EnvSetup
from Config.ConfigSetupWCS import ConfigSetupWCS


class WCSMapFetcher:
    print("Here we go WCS")

    def get_map(self, before_after):
        env_setup = EnvSetup.EnvSetup()

        config = SHConfig()
        config.sh_client_id = env_setup.client_Id
        config.sh_client_secret = env_setup.client_secret
        config.instance_id = env_setup.instance_id

        config_setup = ConfigSetupWCS(before_after=before_after)

        wcs_bands_request = WcsRequest(
            time=config_setup.time_range,
            config=config,
            maxcc=config_setup.cloud_coverage,
            data_collection=DataCollection.SENTINEL2_L2A,
            layer=config_setup.layer,
            bbox=BBox(bbox=config_setup.coords_wgs84_WCS, crs=CRS.WGS84),
            image_format=MimeType.TIFF,
            data_folder=config_setup.data_folder,
            resx=config_setup.resX,
            resy=config_setup.resY,
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
