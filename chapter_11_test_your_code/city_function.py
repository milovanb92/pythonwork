def get_city_state(city, state, population=''):
    """Generate a neatly formated full name"""
    if population:
        city_state = f"{city}, {state} - population {population}"
    else:
        city_state = f"{city}, {state}"
    return city_state.title()

