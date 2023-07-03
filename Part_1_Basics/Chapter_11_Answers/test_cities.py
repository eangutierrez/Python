import unittest

# Problem 11.1
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests the city_functions.py relationship."""

    def test_city_country(self):
        """Completes a city=country pair test."""
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()

# Problem 11.2
from modified_city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests the city_functions.py relationship."""

    def test_city_country(self):
        """Completes a city=country pair test."""
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()
