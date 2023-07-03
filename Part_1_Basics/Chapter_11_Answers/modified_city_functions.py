"""This is a collection of functions for working with cities."""

def city_country(city, country, population=0):
    """Returns a comma-separated string of a city and its respective country"""
    
    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f", population: {population}"
    return output_string