import unittest
from model.cnn_model import create_model

class TestCNNModel(unittest.TestCase):
    def test_model_output(self):
        model = create_model()
        self.assertEqual(model.output_shape, (None, 10))

if __name__ == '__main__':
    unittest.main()
