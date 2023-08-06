class FilterExtractor():
    def __init__(self, model):
        self.model = model
        self.module_filters_map = None

    def get_module_filters_map(self):
        if(self.module_filters_map == None):
            raise ValueError()
        else:
            return self.module_filters_map

    def extract(self):
        if(self.model == None):
            raise ValueError()
        else:
            self.module_filters_map = {}
            self.extract_filters(self.model)

    def extract_filters(self, parent_model):
        if len(parent_model._modules) > 0:
            for module in parent_model._modules:
                self.extract_filters(parent_model._modules[module])
        else:
            if parent_model.__class__.__name__ == 'Conv2d':
               self.module_filters_map[parent_model] = parent_model._parameters['weight'].data


