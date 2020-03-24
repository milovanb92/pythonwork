import json

filename = 'favnum.json'

with open(filename) as f:
    number = json.load(f)
    print(f"I know your favorite number is {number}")