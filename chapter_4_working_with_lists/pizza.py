pizzas = ['capricoza', 'margarita', 'mexicana']
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza!")
print("I really love pizza!!!")

friends_pizzas = pizzas[:]
first_three = pizzas[:3]
print(f"The first three items in list pizzas are {pizzas[0:3]}")
pizzas.append('chilli')
friends_pizzas.append('vegetariana')

print(pizzas)
print(friends_pizzas)

for pizza in pizzas:
    print(f"My favorite pizzas are: {pizza}")

for pizza in friends_pizzas:
    print(f"Friends favorite pizzas are: {pizza}")