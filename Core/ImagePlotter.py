import numpy as np
from matplotlib import pyplot as plt


def plot_image(image, factor=1):
    """
    Utility function for plotting RGB images.
    """
    plt.subplots(nrows=1, ncols=1, figsize=(15, 7))

    if np.issubdtype(image.dtype, np.floating):
        plt.imshow(np.minimum(image * factor, 1))
    else:
        plt.imshow(image * factor)


def plot_image_layout(image_to_plot, aspect_ratio, factor=1):
    # some stuff for pretty plots
    ncols = 2
    nrows = 2
    subplot_kw = {"xticks": [], "yticks": [], "frame_on": False}

    fig, axs = plt.subplots(ncols=ncols, nrows=nrows, figsize=(5 * ncols * aspect_ratio, 5 * nrows),
                            subplot_kw=subplot_kw)

    for idx, image in enumerate(image_to_plot):
        ax = axs[idx // ncols][idx % ncols]
        ax.imshow(np.clip(image * factor, 0, 1))
        ax.set_title(f"{idx}", fontsize=10)

    plt.tight_layout()


class ImagePlotter:
    pass
