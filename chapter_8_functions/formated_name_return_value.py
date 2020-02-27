# def get_formated_name(first_name, last_name):
#     """Return a full anme, neatly formated."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formated_name('jimi', 'hendrix')
# print(musician)


### middle name as optional argument so parameter goes to last place 
def get_formated_name(first_name, last_name, middle_name=''):
    """Return a full anme, neatly formated."""
    # python interprets non-empty string as true, so if we enter middle name it will be true, if not else is executed
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formated_name('jimi', 'hendrix')
print(musician)
musician = get_formated_name('jimi', 'hendrix', 'lee')
print(musician)

