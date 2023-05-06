import os
import geopandas as gpd
import rasterio
from rasterio.mask import mask


class Masker:

    def split_image(self, before_after, main_image_path, geojson_path):
        # Görüntü dosyasını yükleyin
        with rasterio.open(main_image_path) as src:
            # Read the GeoJSON file and extract the geometry of the polygons
            shapefile = gpd.read_file(geojson_path)
            # Get the styleUrl value from the GeoJSON file

            for i, polygon in enumerate(shapefile.geometry):
                style_url = shapefile['styleUrl'][i]
                out_filename = f'Image/2.masked/{before_after}/{style_url}.tiff'

                # Görüntüyü maskeleyin
                out_image, out_transform = mask(src, [polygon], crop=True)
                # Yeni TIFF dosyasını oluşturun
                out_file_path = f'Image/2.masked/{before_after}'
                if not os.path.exists(out_file_path):
                    os.makedirs(out_file_path)
                with rasterio.open(out_filename, 'w', driver='GTiff',
                                   width=out_image.shape[2], height=out_image.shape[1],
                                   count=src.count, crs=src.crs, transform=out_transform,
                                   dtype=out_image.dtype) as dst:
                    # Maskeleme sonucunu yeni TIFF dosyasına kaydedin
                    dst.write(out_image)
                    print(f"Masked image saved as {os.path.abspath(out_filename)}")
