import io

from PIL import Image
from torchvision import transforms

import matplotlib.pyplot as plt
import numpy as np
from skimage import transform


def plot_tensor(tensor):
    results = transforms.ToPILImage()(tensor)
    print(type(results))
    results.show()


def save_tensor_as_image(tensor, filepath):
    results = transforms.ToPILImage()(tensor)
    results.save(filepath)


def plot_tensor_with_heatmap(pil_img, pixel_weight_array):
    add_heatmap(np.asarray(pil_img), pixel_weight_array, display=True)


def save_tensor_with_heatmap(pil_img, pixel_weight_array, filepath, cmap='viridis'):
    add_heatmap(np.asarray(pil_img), pixel_weight_array, display=False, axis='off', save=filepath, cmap=cmap)


import io

from PIL import Image
from torchvision import transforms
from PIL import ImageFilter
import matplotlib.pyplot as plt
import numpy as np
from skimage import transform


def plot_tensor(tensor):
    results = transforms.ToPILImage()(tensor)
    print(type(results))
    results.show()


def save_tensor_as_image(tensor, filepath):
    results = transforms.ToPILImage()(tensor)
    results.save(filepath)


def plot_tensor_with_heatmap(pil_img, pixel_weight_array):
    add_heatmap(np.asarray(pil_img), pixel_weight_array, display=True)


def save_tensor_with_heatmap(pil_img, pixel_weight_array, filepath=None, cmap='viridis'):
    return add_heatmap(np.asarray(pil_img), pixel_weight_array, display=False, axis='off', save=filepath, cmap=cmap)


def add_heatmap(image, heat_map, alpha=0.6, display=False, save=None, cmap='viridis', axis='on', verbose=False):
    height = image.shape[0]
    width = image.shape[1]

    # resize heat map
    heat_map_resized = transform.resize(heat_map, (height, width))

    # normalize heat map
    max_value = np.max(heat_map_resized)
    min_value = np.min(heat_map_resized)
    normalized_heat_map = (heat_map_resized - min_value) / (max_value - min_value)

    # display
    plt.axis(axis)
    fig = plt.imshow(image, interpolation='nearest')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    axes_img = plt.imshow(255 * normalized_heat_map, alpha=alpha, cmap=cmap)

    input_pil_image = Image.fromarray(image)

    #plt.show
    scaled_img = (axes_img.get_array() - axes_img.get_clim()[0]) / (axes_img.get_clim()[1] - axes_img.get_clim()[0])
    heatmap_image = Image.fromarray(np.uint8(axes_img.get_cmap()(scaled_img) * 255))
    plt.imshow(np.asarray(heatmap_image))
    input_pil_image = Image.blend(input_pil_image.convert('RGBA'), heatmap_image, alpha=0.5)

    if display:
        plt.show()

    if save is not None:
        if verbose:
            print('save image: ' + save)
        plt.savefig(save, bbox_inches='tight', pad_inches=0)

    return input_pil_image


