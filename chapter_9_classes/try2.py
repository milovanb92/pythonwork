class User:
    def __init__(self, first_name, last_name, user_age, hair_color):
        self.first = first_name
        self.last = last_name
        self.age = user_age
        self.hair = hair_color
        self.login_attempts = 0
    
    def describe_user(self):
        print("\nThis are information about user: ")
        print(f"\tFirst name is: {self.first} \n\tLast name is: {self.last} \n\tUser age: {self.age} \n\tHair color: {self.hair} \n\tLogin Attempts: {self.login_attempts}")
        print("\nUser have next permissions: ")

    def greet_user(self):
        print(f"Thank you for joining us {self.first} {self.last}")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        
class Privileges:
    def __init__(self, privileges=["Can add user", "Can delete user", "Can modify posts"]):
        self.privileges = privileges

    def show_privileges(self):
        #print(f"The user: \n{self.first} {self.last} \nhave next privileges: ")
        for privilege in self.privileges:
            print(f"\t{privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, user_age, hair_color):
        super().__init__(first_name, last_name, user_age, hair_color)
        self.privileges = Privileges()
    


user1 = Admin('Milovan', 'Bekic', 27, 'Brown')
user2 = User('Kico', 'Marjanovic', 28, 'Black')
user3 = User('Marko', 'Vukovic', 27, 'Black')

# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()

# user1.describe_user()

# user1.reset_login_attempts()
# user1.describe_user()
# user1.greet_user()

user1.describe_user()
user1.privileges.show_privileges()
