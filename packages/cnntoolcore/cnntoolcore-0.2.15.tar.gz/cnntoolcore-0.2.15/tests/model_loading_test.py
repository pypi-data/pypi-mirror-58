import unittest

from torch_model_loading.model_loader import ModelLoader


class ModelLoadingTests(unittest.TestCase):
    def test_should_load_model(self):
        loader = ModelLoader()
        model = loader.load_model_from_external_file('test_model.py')
        self.assertNotEquals(model, None)