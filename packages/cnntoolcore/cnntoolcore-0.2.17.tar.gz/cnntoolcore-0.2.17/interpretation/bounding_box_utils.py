import math
import numpy as np
from PIL import Image


class BoundingBoxUtils:

    # pil image in rgb
    @staticmethod
    def get_bounding_boxes_from_image(pil_image):
        im = pil_image.convert('RGB')
        pixVals = set(im.getdata())
        img = np.array(im)
        color_box_map = {'#%02x%02x%02x' % rgb_tuple: [math.inf, math.inf, -1, -1] for rgb_tuple in pixVals}

        for x in range(img.shape[0]):
            for y in range(img.shape[1]):
                current_pixel = '#%02x%02x%02x' % tuple(img[x][y])
                x1, y1, x2, y2 = color_box_map[current_pixel]

                if x < x1:
                    color_box_map[current_pixel][0] = x
                if x > x2:
                    color_box_map[current_pixel][2] = x
                if y < y1:
                    color_box_map[current_pixel][1] = y
                if y > y2:
                    color_box_map[current_pixel][3] = y

        return color_box_map

    @staticmethod
    # box - x1,y1,x2,y2
    def intersection_over_union(boxA, boxB):
        # determine the (x, y)-coordinates of the intersection rectangle
        xA = max(boxA[0], boxB[0])
        yA = max(boxA[1], boxB[1])
        xB = min(boxA[2], boxB[2])
        yB = min(boxA[3], boxB[3])

        # compute the area of intersection rectangle
        interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

        # compute the area of both the prediction and ground-truth
        # rectangles
        boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
        boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

        # compute the intersection over union by taking the intersection
        # area and dividing it by the sum of prediction + ground-truth
        # areas - the interesection area
        iou = interArea / float(boxAArea + boxBArea - interArea)

        # return the intersection over union value
        return iou

    @staticmethod
    def get_bounding_boxes_from_heatmap(normalized_heapmap):
        percentile = np.percentile(normalized_heapmap, 90)
        normalized_heapmap = normalized_heapmap * (normalized_heapmap > percentile).astype(int)

        maps = []
        color_rectangle_map = {}
        boundaries = []

        while True:
            peak = np.unravel_index(normalized_heapmap.argmax(), normalized_heapmap.shape)

            if normalized_heapmap[peak[0]][peak[1]] == 0:
                break

            out_map = np.zeros_like(normalized_heapmap)
            BoundingBoxUtils.extract_peak(peak, normalized_heapmap, out_map)

            x1 = np.min(np.nonzero(np.sum(out_map, axis=0)))
            y1 = np.min(np.nonzero(np.sum(out_map, axis=1)))
            x2 = np.max(np.nonzero(np.sum(out_map, axis=0)))
            y2 = np.max(np.nonzero(np.sum(out_map, axis=1)))

            normalized_heapmap = np.multiply(normalized_heapmap, -out_map + 1)
            maps.append(out_map.copy())
            boundaries.append((x1, x2, y1, y2))

        return boundaries

    @staticmethod
    def extract_peak(current_pixel, source_map, out_map):
        x, y = current_pixel
        out_map[x][y] = 1

        # Extract left
        if y - 1 >= 0 and out_map[x][y - 1] != 1 and source_map[x][y - 1] < source_map[x][y] and source_map[x][
            y - 1] > 0:
            BoundingBoxUtils.extract_peak((x, y - 1), source_map, out_map)

        # Extract right
        if y + 1 < source_map.shape[1] and out_map[x][y + 1] != 1 and source_map[x][y + 1] < source_map[x][y] and \
                source_map[x][y + 1] > 0:
            BoundingBoxUtils.extract_peak((x, y + 1), source_map, out_map)
        # Extract top
        if x - 1 >= 0 and out_map[x - 1][y] != 1 and source_map[x - 1][y] < source_map[x][y] and source_map[x - 1][
            y] > 0:
            BoundingBoxUtils.extract_peak((x - 1, y), source_map, out_map)
        # Extract bottom
        if x + 1 < source_map.shape[0] and out_map[x + 1][y] != 1 and source_map[x + 1][y] < source_map[x][y] and \
                source_map[x + 1][y] > 0:
            BoundingBoxUtils.extract_peak((x + 1, y), source_map, out_map)
