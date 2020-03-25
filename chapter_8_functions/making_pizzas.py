# importing module pizza (pizza.py file in same dir)
import pizza
# calling module and function: module_name.function_name()    -   function in that module
pizza.make_pizza('big', 'peperoni')
pizza.make_pizza('small', 'mushrooms', 'green pepers', 'extra cheese')

# we can also import just one or more function from a moduel
from pizza import make_pizza
# and call just a function
make_pizza('big', 'peperoni')
make_pizza('small', 'mushrooms', 'green pepers', 'extra cheese')

# import function from module by renaming it (make alias) if name is too long or existing in current program
from pizza import make_pizza as mp 
mp('big', 'peperoni')
mp('small', 'mushrooms', 'green pepers', 'extra cheese')

# import module as alias 
import pizza as p
p.make_pizza('big', 'peperoni')
p.make_pizza('small', 'mushrooms', 'green pepers', 'extra cheese')

# import all function from a module with *
from pizza import *
make_pizza('big', 'peperoni')
make_pizza('small', 'strumf', 'green pepers', 'extra cheese')
