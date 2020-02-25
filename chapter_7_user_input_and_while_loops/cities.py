prompt = "\nPlease enter the name of city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"


# the loop that start with "while True:" will run forever until it reaches "break" statement
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
