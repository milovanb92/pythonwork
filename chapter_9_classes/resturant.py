"""The module that represents resturant"""

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