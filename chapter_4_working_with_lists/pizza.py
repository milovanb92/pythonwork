pizzas = ['capricoza', 'margarita', 'mexicana']
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza!")
print("I really love pizza!!!")

friends_pizzas = pizzas[:]

pizzas.append('chilli')
friends_pizzas.append('vegetariana')

print(pizzas)
print(friends_pizzas)

for pizza in pizzas:
    print(f"My favorite pizzas are: {pizza}")

for pizza in friends_pizzas:
    print(f"Friends favorite pizzas are: {pizza}")