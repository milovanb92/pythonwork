import json

filename = 'favnum.json'

try:
    with open(filename) as f:
        number = json.load(f)
        print(f"I know your favorite number is {number}")
except FileNotFoundError:
    number = input("Enter your favorite number: ")
    with open(filename, 'w') as f:
        json.dump(number, f)

