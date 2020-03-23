"""Admin and privileges module """
from user import User

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