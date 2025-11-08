import unittest
import math

def get_sqrt(n):
    return math.sqrt(n)

def divide(a, b):
    return a / b

class TestUnexpected(unittest.TestCase):
    
    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            get_sqrt(-144)
        
    def test_sqrt_positive(self):
        result = get_sqrt(144)
        self.assertEqual(result, 12)

    def test_divide(self):
        result = divide(144, 12)
        self.assertEqual(result, 12)
    
    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(144, 0)

if __name__ == '__main__': 
    unittest.main()