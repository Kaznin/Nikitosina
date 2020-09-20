import unittest
import GET_SUM from GET_SUM

class TestGET_SUM(unittest.TestCase):
    def test_equal_ten(self):
        result = func(10)
        self.assertIsNotNone(result)
        self.assertEqual(10, result)