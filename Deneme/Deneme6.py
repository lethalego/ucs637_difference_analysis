import numpy as np
from sklearn.cluster import KMeans
from PIL import Image

# Load image
img1 = Image.open("../Deneme/Image/Before/20230127.png")
img1_data = np.array(img1)

# Flatten the image data
img1_data_flat = img1_data.reshape(-1, img1_data.shape[-1])

# Run KMeans on the flattened data
kmeans = KMeans(n_clusters=3, random_state=0).fit(img1_data_flat)
labels = kmeans.labels_

# Reshape the labels back into the original image shape
img1_clusters = labels.reshape(img1_data.shape[:2])

# Save the clustered image
img1_clusters_rgb = np.zeros_like(img1_data)
for i in range(3):
    img1_clusters_rgb[:, :, i] = (img1_clusters == i) * 255
img1_clusters_rgb = Image.fromarray(img1_clusters_rgb)
img1_clusters_rgb.save("test_image_clustered.png")