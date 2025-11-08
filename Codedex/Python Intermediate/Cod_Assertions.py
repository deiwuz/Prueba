import unittest
from string_utils import reverse_string, capitalize_string, is_capitalized

class TestStringUtils(unittest.TestCase):
    def test_reverse(self):
        result = reverse_string("Hola")
        er = "aloH"
        self.assertEqual(result, er)
    
    def test_capitalize(self):
        result = capitalize_string("hola")
        er = "Hola"
        self.assertEqual(result, er)
    
    def test_is_capitalized_True(self):
        self.assertTrue(is_capitalized("Hola"))

    def test_is_capitalized_False(self):
        self.assertFalse(is_capitalized("hola"))

if __name__ == '__main__':
  unittest.main()