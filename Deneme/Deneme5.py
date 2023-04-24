from sklearn.cluster import KMeans
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Load the image
img = Image.open('../Deneme/Image/After/20230209.Png')

# Convert the image to RGB mode
img = img.convert('RGB')

# Convert the image to a numpy array
img_array = np.array(img)

# Reshape and resize the image
img_reshaped = img_array.reshape((-1, 3))

# Create a k-Means object
kmeans = KMeans(n_clusters=5, random_state=0)

# Perform the k-Means clustering
labels = kmeans.fit_predict(img_reshaped)

# Count the number of pixels in each class
counts = np.bincount(labels)

# Get the RGB color values of the cluster centers
colors = kmeans.cluster_centers_

# Create a color map based on the k-means cluster centroids
color_map = ListedColormap(colors / 255)

# Map each pixel value to the corresponding color
classified_img = color_map(labels.reshape(img_array.shape[:2]))

# Display the original and classified images side by side
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(img)
axs[0].set_title('Original Image')
axs[1].imshow(classified_img)
axs[1].set_title('Classified Image')
axs[1].set_xticks([])
axs[1].set_yticks([])

# Add color legend for the classes
handles = [plt.plot([], [], marker="o", ls="", color=colors[i] / 255)[0] for i in range(len(colors))]
labels = ['Class {} ({:,d} pixels)'.format(i + 1, count) for i, count in enumerate(counts)]
axs[1].legend(handles, labels, loc='lower center', bbox_to_anchor=(-0.5, -0.6), ncols=2)

plt.show()

# Save the classified image as a PNG
classified_img = Image.fromarray((classified_img * 255).astype(np.uint8))
classified_img.save('sınıflandırılmış_goruntu2.png', 'PNG')
