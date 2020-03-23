from users import Admin, Privileges

user = Admin('Milovan', 'Bekic', 27, 'Brown')
user.describe_user()
user.privileges.show_privileges()