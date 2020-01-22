person = {'first_name': 'kico', 'last_name': 'marjanovic', 'age': 28, 'city': 'banjaluka'}
print(f"{person['first_name'].title()}")
print(f"{person['last_name'].title()}")
print(f"{person['age']}")
print(f"{person['city'].title()}")

favorite_number = {
    'kico': 17,
    'sreco': 19,
    'marko': 55,
    'sasa': 27,
    'kole': 33,
}
print(f"Favorite number is {favorite_number['kico']}")
print(f"Favorite number is {favorite_number['sreco']}")
print(f"Favorite number is {favorite_number['marko']}")
print(f"Favorite number is {favorite_number['sasa']}")
print(f"Favorite number is {favorite_number['kole']}")


favorite_number = {
    'kico': [15, 24],
    'sreco': [22, 52],
    'marko': [43, 11],
    'sasa': [28, 42],
    'kole': [33, 56],
}

for name, numbers in favorite_number.items():
    print(f"{name.title()} favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")