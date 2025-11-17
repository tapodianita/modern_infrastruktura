import unittest
from modern_infrastruktura import addition

class TestAddition(unittest.TestCase):

    def test_psotive(self):
        self.assertEqual(addition(5, 7), 12)

    def test_zero(self):
        self.assertEqual(addition(0, 10), 10)

    def test_negative(self):
        self.assertEqual(addition(-3, -4), -7)

    def test_negative_positive(self):
        self.assertEqual(addition(-3, 7), 4)

if __name__ == "__main__":
    unittest.main()

