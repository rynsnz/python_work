def city_country(city, country):
    """Return a properaly formatted City and County..."""
    return f"{city.title()}, {country.title()}"

print(city_country('san diego', 'united states'))
print(city_country('everett', 'united states'))
print(city_country('chicago', 'united states'))