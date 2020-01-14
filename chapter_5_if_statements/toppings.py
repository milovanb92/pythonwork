requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese.")

print("\nFinished making your pizza.")


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry we don't have more green peppers")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# define empty list
requested_toppings = []
# when the name of list is used in if statement, python returns TRUE if list contains at least one item
# if list is empty Python returns FALSE
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza")
else:
    print("\nAre you sure you want a plain pizza?")
print()

# adding multiple list, and we loop through second list to se if items are available in first list
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza.")