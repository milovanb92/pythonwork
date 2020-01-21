rivers = {
    'nile': 'egypt',
    'amazon': 'brasil',
    'dunav': 'srbija',
}

for river, state in rivers.items():
    print(f"The {river.title()} runs through {state.title()}")

for river in rivers.keys():
    print(river.title())

for state in rivers.values():
    print(state.title())