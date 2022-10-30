cities = {
    'mexico city': {
        'country': 'mexico',
        'population': 21_581_000,
        'fact': "Mexico's capital is both the oldest capital city in the Americas and one of two founded by indigenous people.",
    },

    'delhi': {
        'country': 'india',
        'population': 28_514_000,
        'fact': '...',
    },

    'tokyo': {
        'country': 'japan',
        'population': 37_468_000,
        'fact': 'Tokyo is the capital and largest city in Japan.',
    },
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    
    print(f"\tCountry: {city_info['country'].title()}")
    print(f"\tPopulation Estimate: {city_info['population']}")
    print(f"\tFact: {city_info['fact']}")