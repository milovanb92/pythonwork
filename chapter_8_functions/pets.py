# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")
# #keyword arguments order doesn't matter
# describe_pet(animal_type='konj', pet_name='jovan')

def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")
describe_pet(pet_name='sasa')
describe_pet(pet_name='mikan', animal_type='konj')

###   When you use default values, any parameter with a default value needs to be listed -
###   after all the parameters that don’t have default values. This allows Python to continue interpreting positional arguments correctly.