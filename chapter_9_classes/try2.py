class User:
    def __init__(self, first_name, last_name, user_age, hair_color):
        self.first = first_name
        self.last = last_name
        self.age = user_age
        self.hair = hair_color
    
    def describe_user(self):
        print("\nThis are information about user: ")
        print(f"\tFirst name is: {self.first} \n\tLast name is: {self.last} \n\tUser age: {self.age} \n\tHair color: {self.hair}")

    def greet_user(self):
        print(f"Thank you for joining us {self.first} {self.last}")

user1 = User('Milovan', 'Bekic', 27, 'Brown')
user2 = User('Kico', 'Marjanovic', 28, 'Black')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()