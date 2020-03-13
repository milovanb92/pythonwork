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

resturant = Resturant('Kanjoj', 'Domaca')

# print(f"My resturant is called {resturant.name}")
# print(f"Cuisine in my resturant is {resturant.cuisine}")
# resturant.describe_resturant()
# resturant.open_resturant()

# resturant2 = Resturant('Konoba', 'Rostilj')
# print(f"Moj restoran je {resturant2.name} a najbolji im je {resturant2.cuisine}.")
# resturant2.describe_resturant()

# resturant3 = Resturant('Zlatna kruna', 'Ope Rostilj')
# print(f"Moj restoran je {resturant3.name} a imaju {resturant3.cuisine}.")
# resturant3.describe_resturant()

resturant.set_number_served(4)
resturant.increment_number_served(3)
print(f"Number of served customers are {resturant.number_served}")