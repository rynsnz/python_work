favorite_places = {
    'ryan': ['san diego', 'las vegas', 'honolulu'],
    'poe': ['everett'],
    'erwin': ['brooklyn', 'chicago', 'hilo']
}

for person, places in favorite_places.items():
    if len(places) == 1:
        print(f"{person.title()}'s favorate place is {places[0].title()}.")
    else:
        print(f"{person.title()}'s favorate places are:")
        for place in places:
            print(f"\t{place.title()}")