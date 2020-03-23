from car1 import Car
from electric_car1 import ElectricCar
from electric_car1 import ElectricCar as EC

my_beetle = Car('vw', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla2 = EC('tesla', 'roadster', 2018)
print(my_tesla2.get_descriptive_name())