# * ispred parametra za funkciju znaci da mozemo za parametar proslijediti proizvoljan broj argumenata 
# ako miksamo pozicione i proizvoljne argumente, onda parametar za proizvoljne argumente stavljamo na kraj *toppings
def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    print(f"\nMaking a {size} pizza with following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# velicinu pizze stavljamo na pocetak zbog pozicionog argumenta koji proslijedjujemo funkicji
make_pizza('big', 'peperoni')
make_pizza('small', 'mushrooms', 'green peppers', 'extra cheese')
