import unittest
from modern_infrastruktura import addition


class TestCalculatorIntegration(unittest.TestCase):
    
    def test_multiple_operations(self):
        result1 = addition(3, 4)
        result2 = addition(result1, 5)
        self.assertEqual(result2, 12)
 
    
    def test_shopping_cart(self):
        x = 15
        y = 15
        
        total = addition(x, y)
        self.assertEqual(total, 30)
    

if __name__ == '__main__':
    unittest.main(verbosity=2)




