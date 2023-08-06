import unittest

import torchvision

from visualization_utils.hook_utils import HookUtils



class HookUtilsTest(unittest.TestCase):
    def hook_fn(m, i, o):
        pass

    def test_should_register_hook(self):
        model = torchvision.models.AlexNet()

        HookUtils.deep_hook_register(model, self.hook_fn)

        self.assertEquals(len(model._modules['features']._modules['0']._forward_hooks), 1)