car = input("What kind of rental car you want? ")
print(f"\nLet me see if I can find you a {car}.")
 
print("......")

dinner_group = input("\nHow many people comming to resturant in a group? ")
number = int(dinner_group)
if number > 8:
    print("Sorry, you need to wait for a table.")
else:
    print("Your table is ready.")

print(".........")

number = input("Please enter some number and I will tell you if the number multiple with 10: ")
number = int(number)
if number % 10 == 0:
    print("Djeljiv")
else:
    print("Nije")