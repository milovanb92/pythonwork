# def greet_user():
#     """Display a simple greeting."""
#     print("Hello!")

# greet_user()

# def greet_user(username):
#     """Display a simple greeting."""
#     print(f"Hello, {username.title()}!")
# greet_user('milovan')

def get_formated_name(first_name, last_name):
    """Return a full anme, neatly formated."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an inifite loop!
while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break


    formatted_name = get_formated_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
