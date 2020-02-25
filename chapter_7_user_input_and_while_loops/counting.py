currrent_number = 1
while currrent_number <= 5:
    print(currrent_number)
    currrent_number += 1     #  broj += 1   je isto sto i    broj = broj + 1 , inkrement za 1 

print("\n")

currrent_number = 0
while currrent_number < 10:
    currrent_number += 1
    if currrent_number % 2 == 0:
        continue
    print(currrent_number)

print("\n")

x = 1
while x <= 5:
    print(x)
    x += 1  # without this line we would make infinite loop