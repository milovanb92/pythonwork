# dvije ** ispred parametra u funkciji govore Python-u da napravi prazan rijecnik (dictionary) nazvan user_info 
# i smijesta sve key-value pairs u njega
# u funkciji mozemo koristiti key-value pairs iz user_info kao da je bilo koji rijecnik
def build_profile(first, last, **user_info):
    """Building a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)