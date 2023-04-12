import numpy as np
import rasterio
from matplotlib import pyplot as plt
from rasterio.plot import show
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
from rasterio.errors import NotGeoreferencedWarning
import warnings

# Suppress georeferencing warning
warnings.filterwarnings("ignore", category=NotGeoreferencedWarning)

# Load two satellite images
with rasterio.open('../Deneme/Image/Before/20230127.Png') as src:
    img1 = src.read()
    profile1 = src.profile

with rasterio.open('../Deneme/Image/After/20230209.png') as src:
    img2 = src.read()
    profile2 = src.profile

# Compute difference between two images
img_diff = img2 - img1



# Normalize pixel values
norm_diff = normalize(img_diff.reshape(img_diff.shape[0], -1))
norm_diff = norm_diff.reshape(img_diff.shape)



# Compute PCA
pca = PCA(n_components=2, tol=1e-8)
cva = pca.fit_transform(norm_diff.reshape(norm_diff.shape[0], -1))
variances = pca.explained_variance_
components_to_keep = variances > 0
cva = cva[:, components_to_keep]

# Show results
fig, ax = plt.subplots()
show(cva, ax=ax)
ax.set_xlabel('Component 1 ({:.2f}% explained variance)'.format(variances[0]*100))
ax.set_ylabel('Component 2 ({:.2f}% explained variance)'.format(variances[1]*100))
ax.set_title('Change Vector Analysis')
plt.show()

