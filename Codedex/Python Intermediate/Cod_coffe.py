# Write code below 💖

import unittest

class CoffeeMenu:
    def __init__(self):
        self.menu = {
    'espresso': 2.50,
    'latte': 2.75,
    'cappuccino': 3.20,
    'americano': 2.70
    }

    def get_price_existing_item(self, i):
        return self.menu[i]
    def get_price_non_existing_item(self, i):
        if i not in self.menu:
            return False
        else:
            return True
    def add_item(self, i, p):
        if p <= 0:
            raise ValueError("Price must be positive")
        self.menu[i] = p
        return True
    def show_menu(self):
        for (i, v) in self.menu.items():
            print(f"{i}, {v}$")

class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.coffeeshop = CoffeeMenu()
    
    def tearDown(self):
        self.coffeeshop = None

    def test_get_price_existing_item(self):
        expected_result = 2.5
        self.assertEqual(self.coffeeshop.get_price_existing_item("espresso"), expected_result)
    
    def test_get_price_non_existing_item(self):
        with self.assertRaises(KeyError):
            self.coffeeshop.get_price_existing_item("coffee")
    
    def test_add_item(self):
        self.assertTrue(self.coffeeshop.add_item("coffee", 20))

if __name__ == '__main__':
  unittest.main()