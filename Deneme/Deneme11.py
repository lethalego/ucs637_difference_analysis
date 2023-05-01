from PIL import Image, ImageOps
import numpy as np

image1 = Image.open("../Deneme/Image/before.png").convert("L")
image_array = np.array(image1)

normalized_image = (image_array - np.min(image_array)) / (np.max(image_array) - np.min(image_array))
normalized_image = (normalized_image * 255).astype(np.uint8)
normalized_image = Image.fromarray(normalized_image)

img1 = ImageOps.equalize(normalized_image)

normalized_image.save("Output/Deneme11_before_1.png")
img1.save("Output/Deneme11_before_2.png")
