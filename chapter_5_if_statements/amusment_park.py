age = 2

if age < 4:
    print("You admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("You admission cost is $40.")

# another example

age = 64

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")
