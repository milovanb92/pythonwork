# sandwich_orders = ['kulen', 'sunka', 'peka', 'kulen', 'tuna', 'kulen']
# finished_sandwich = []

# while 'kulen' in sandwich_orders:
#     sandwich_orders.remove('kulen')
# print("We run out of kulen")

# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print(f"Making you a {sandwich} sandwich.")
#     finished_sandwich.append(sandwich)

# for sandwich in finished_sandwich:
#     print(f"{sandwich} is finished.")

vocation = {}

poll_active = True

while poll_active:
    name = input("\nWhat is your name? " )
    place = input("Which place you would like to visit? ")
    vocation[name] = place

    repeat = input("\nWould you like to continue poll? (yes/no) ")
    if repeat == 'no':
        poll_active = False

for name, place in vocation.items():
    print(f"{name.title()} would like to visit {place.title()}")