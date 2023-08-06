from importlib._bootstrap_external import SourceFileLoader

class ModelLoader():
    #Loading torch_model_loading variable from file with name set by convention as 'torch_model_loading'
    def load_model_from_external_file(self,filepath):
        model_file = SourceFileLoader('conf', filepath).load_module()
        return model_file.model

    def load_input_shape_from_external_file(self,filepath):
        model_file = SourceFileLoader('conf', filepath).load_module()
        return model_file.input_shape

