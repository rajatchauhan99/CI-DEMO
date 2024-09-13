import unittest
from app import sum, sub, mul  # Replace 'your_module_name' with the actual module name

class TestMathOperations(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(9, 10), 19)
        self.assertEqual(sum(-1, 1), 0)
        self.assertEqual(sum(0, 0), 0)

    def test_sub(self):
        self.assertEqual(sub(10, 2), 8)
        self.assertEqual(sub(0, 5), -5)
        self.assertEqual(sub(5, 5), 0)

    def test_mul(self):
        self.assertEqual(mul(10, 2), 20)
        self.assertEqual(mul(0, 10), 0)
        self.assertEqual(mul(-1, 10), -10)

if __name__ == '__main__':
    unittest.main()
