import unittest

from modified_city_functions import city_country

class CitiesTestCase(unittest.TestCase): 
    """Tests the city_functions.py relationship."""

    def test_city_country(self):
        """Completes a city-country pair test."""
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')

    def test_city_country_population(self):
        """Completes a city-country-population test."""
        santiago_chile = city_country('santiago', 'chile', population=5000000)
        self.assertEqual(santiago_chile, 'Santiago, Chile, population: 5000000')


if __name__ == '__main__':
    unittest.main()