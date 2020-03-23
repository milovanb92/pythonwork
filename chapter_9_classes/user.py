"""User module"""

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