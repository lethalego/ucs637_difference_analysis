from sklearn.cluster import KMeans
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

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

# Reshape the labels and create a classified image
labels_reshaped = labels.reshape(img_array.shape[0], img_array.shape[1])
classified_img = Image.fromarray(np.uint8(labels_reshaped))

# Display the original and classified images side by side
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(img)
axs[0].set_title('Orjinal')
axs[1].imshow(classified_img)
axs[1].set_title('Sınıflandırılmış')
plt.show()

# Save the classified image as a PNG
classified_img.save('sınıflandırılmış_goruntu3.png', 'PNG')
