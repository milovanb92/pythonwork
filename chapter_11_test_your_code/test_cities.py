import unittest
from city_function import get_city_state

class CityTestCase(unittest.TestCase):
    """Test for city_function.py"""

    def test_city_state(self):
        """Does formating like Knezevo, Bih working?"""
        city_format = get_city_state('knezevo', 'bih')
        self.assertEqual(city_format, 'Knezevo, Bih')

    def test_city_state_population(self):
        """Does formating like Knezevo, Bih - population 10000 working?"""
        city_format = get_city_state('knezevo', 'bih', 10000)
        self.assertEqual(city_format, 'Knezevo, Bih - Population 10000')

if __name__ == '__main__':
    unittest.main()