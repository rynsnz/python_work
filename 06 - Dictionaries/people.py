person_0 = {
    'first_name': 'poe',
    'last_name': 'kappa',
    'age': 3,
    'city': 'honolulu'
}

person_1 = {
    'first_name': 'ryan',
    'last_name': 'kappa',
    'age': 28,
    'city': 'honolulu'
}

person_2 = {
    'first_name': 'erweezy',
    'last_name': 'kappa',
    'age': 26,
    'city': 'honolulu'
}

people = [person_0, person_1, person_2]

#for trait, value in person_0.items():
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name.title()} is {person['age']} and lives in {person['city'].title()}")