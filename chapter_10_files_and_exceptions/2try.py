# prompt = "Please enter your name: "
# prompt += "\n pres 'q' to quit\n"
filename = 'text_files/guest_book.txt'

active = True

while active:
    name = input("Please enter your name: ")
    if name == 'q':
        active = False
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{name}\n")
            print(f"Thank you for your visit {name}")
            