usernames = ['miki', 'kico', 'marko', 'micko', 'admin']

for user in usernames:
    if user == 'admin':
        print("Hello admin, would you lke to see a status report?")
    else:
        print(f"Thank you for login {user}!")

usernames = []
if usernames:
    print("List is not empty!")
else:
    print("We need to find users!")


current_users = ['miki', 'kico', 'marko', 'micko', 'admin']
new_users = ['sasa', 'bobo', 'marko', 'sreco', 'admin']

for user in new_users:
    if user in current_users:
        print(f"{user} username is used, please enter new one!")
    else:
        print(f"{user} username is available!")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
