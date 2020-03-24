def get_fomanted_name(first, last, middle=''):
    """Generate a neatly formated full name"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

