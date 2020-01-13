cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Try it yourself

cars = ['audi', 'bmw', 'subaru', 'toyota']
car1 = 'bmw'
car2 = 'mazda'
if car1 not in cars or car2 not in cars:
    print("On of cars not in a list!")
else:
    print("cars are in a list")

cars = ['audi', 'bmw', 'subaru', 'toyota', 'mazda']
car1 = 'bmw'
car2 = 'mazda'
if car1 not in cars or car2 not in cars:
    print("On of cars not in a list!")
else:
    print("cars are in a list")


car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

if car == 'Subaru':
    print("\nCar is Subaru!")
else:
    print("\nNot Subaru!")

if car.title() == 'Subaru':
    print("\nCar is Subaru!")
else:
    print("\nNot Subaru!")


