from sklearn.cluster import KMeans
import numpy as np
from PIL import Image

# Load the image
img = Image.open('../Deneme/Image/Before/20230127.Png')

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

# Save the classified image as a JPEG
classified_img.save('sınıflandırılmış_goruntu.jpg', 'JPEG')
