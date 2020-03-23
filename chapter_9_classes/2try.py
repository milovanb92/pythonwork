class Resturant:
    def __init__(self, resturant_name, cuisine_type):
        self.name = resturant_name
        self.cuisine = cuisine_type
        self.number_served = 1
    
    def describe_resturant(self):
        print(f"Name of this resturatn is {self.name} and cuisine is {self.cuisine}")
    
    def open_resturant(self):
        print(f"The resturan {self.name} is open.")
    
    def set_number_served(self, served):
        self.number_served = served
    
    def increment_number_served(self, increment):
        self.number_served += increment

class Ice_cream_stand(Resturant):

    def __init__(self, resturant_name, cuisine_type):
        super().__init__(resturant_name, cuisine_type)
        self.flavor = ['jagoda', 'kivi', 'banana']
    
    def list_flavors(self):
        print("Whe have those kind of ice cream flavors: ")
        for item in self.flavor:
            print(f"\t{item}")


my_ice_cream = Ice_cream_stand('kanjon', 'svasta')
print(my_ice_cream.describe_resturant())
print(my_ice_cream.list_flavors())