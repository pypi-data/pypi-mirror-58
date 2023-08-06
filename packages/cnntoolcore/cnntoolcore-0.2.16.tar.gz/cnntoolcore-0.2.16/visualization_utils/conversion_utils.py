
class ConversionUtils:
    @staticmethod
    def convert_3d_map_to_list_of_2d_maps(tensor_3d_map):
        list_2d_maps = []

        for i in range(tensor_3d_map.shape[0]):
            list_2d_maps.append(tensor_3d_map[i])

        return list_2d_maps