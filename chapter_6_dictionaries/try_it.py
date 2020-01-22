person_0 = {
    'first_name': 'kico',
    'last_name': 'marjanovic', 
    'age': 28, 
    'city': 'banjaluka',
}
person_1 = {
    'first_name': 'sasa',
    'last_name': 'brkic', 
    'age': 27, 
    'city': 'knezevo',
}
person_2 = {
    'first_name': 'bojan',
    'last_name': 'komljenovic', 
    'age': 33, 
    'city': 'prijedor',
}

people = [person_0, person_1, person_2]
for person in people:
    print(person)

favorite_places = {
    'sasa': ['banja luka', 'knezevo', 'brkici'],
    'kico': ['budva', 'knezevo'],
    'sreco': ['kafana', 'diskoteka'],
}

for name, places in favorite_places.items():
    print(f"{name.title()} favorite places are: ")
    for place in places:
        print(f"\t{place.title()}") 


cities = {
    'knezevo': {
        'country': 'bosnia and herzegovina',
        'population': 10000,
        'fact': 'Grad na brdu',
    },
    'banja luka': {
        'country': 'bosnia and herzegovina',
        'population': 150000,
        'fact': 'grad djevojaka',
    },
    'budva': {
        'country': 'montenegro',
        'population': 30000,
        'fact': 'grad na moru',
    },
}

for city, descritpion in cities.items():
    print(f"\n{city.title()}")
    country = descritpion['country']
    population = descritpion['population']
    fact = descritpion['fact']
    print(f"\tDrzava: {country.title()}")
    print(f"\tPopulacija: {population}")
    print(f"\tCinjenica: {fact.title()}")
