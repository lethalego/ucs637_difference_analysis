import geojson as geojson
import geopandas as gpd
import numpy as np
import rasterio
from matplotlib import pyplot as plt
from rasterio.mask import mask

from Config.ConfigSetupWCS import ConfigSetupWCS
from Core.ImagePlotter import plot_image, plot_image_aspect

configSetup = ConfigSetupWCS()

# Open the image file
with rasterio.open('../Deneme/deneme_tiff/e4b8d3e9993ad65bca89d32df5dac0c4/response.tiff') as src:

    # Read the GeoJSON file and extract the geometry of the polygon
    shapefile = gpd.read_file('../resources/AdiyamanGeo.json')
    polygon = shapefile.geometry.values[0]

    # Mask the image with the polygon
    out_image, out_transform = rasterio.mask.mask(src, [polygon], crop=True)

    # Display the masked image

    BLUE_BAND = 2
    GREEN_BAND = 3
    RED_BAND = 4

    red = out_image[RED_BAND]
    green = out_image[GREEN_BAND]
    blue = out_image[BLUE_BAND]

    # 4 3 2 bandı birleşince true color verir
    rgb = np.dstack((red, green, blue))

    # parlaklığı artır

    ratio = (configSetup.coords_wgs84[2] - configSetup.coords_wgs84[0]) / (
            configSetup.coords_wgs84[1] - configSetup.coords_wgs84[3])

    plot_image_aspect(rgb, ratio, factor=2.5 / 255)
    plt.figure(figsize=(100, 100))
    plt.show()

    plt.imshow(out_image[0], cmap=None)
    plt.show()
