import numpy
import torch
from torchvision.transforms import transforms, ToTensor


class ImageProcessing:
    @staticmethod
    def pil_img_to_numpy_array(pil_image):
        return numpy.array(pil_image)

    @staticmethod
    def pil_img_to_tensor_of_with_size(pil_image, img_shape):
        transform = transforms.Compose([
            transforms.Resize((img_shape[1], img_shape[2])),
            ToTensor()
        ])
        return transform(pil_image)

    @staticmethod
    def get_list_off_all_colors(pil_img):
        return set(pil_img.getdata())
