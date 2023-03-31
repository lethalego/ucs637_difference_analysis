import geojson as geojson
from PIL import Image

img = Image.open('path/to/saved/image.png').convert('RGBA')
mask = geojson.get_mask(shape=img.size, target_crs='epsg:4326')
masked_img = img.copy()
masked_img.putalpha(mask)

# Save the masked image
masked_img.save('path/to/save/masked_image.png')
