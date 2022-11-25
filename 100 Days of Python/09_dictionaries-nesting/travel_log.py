travel_log = []

def add_new_country(country, visits, cities):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities
    })

add_new_country("Japan", 7, ["Tokyo", "Fukuoka", "Yokosuka"])
print(travel_log)
