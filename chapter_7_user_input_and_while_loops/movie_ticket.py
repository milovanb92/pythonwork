prompt = "\nPlease enter your age: "
prompt += "\n(Press q to exit) "

age = input(prompt)

while age != 'q':
    age = int(age)
    if age <= 3:
        print("Karta je besplatna.")
        break
    elif age > 3 and age <= 12:
        print("Karta je 10 maraka")
        break
    else:
        print("Karta je 15 maraka")
        break
