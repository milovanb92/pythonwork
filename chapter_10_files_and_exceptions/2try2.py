filename = 'text_files/name_response.txt'
responses = {}
# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Why do you like programming? ")

    # Store response in the dictionary   #  dictionary[key] = value
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Store name and value to a file 
for name, response in responses.items():
    with open(filename, 'a') as file_object:
        file_object.write(f"{name} \t{response}\n")
