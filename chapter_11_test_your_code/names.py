from name_function import get_fomanted_name

print("Enter 'q' at any time to quit.")

while True:
    first = input("\nPlease enter a first name: ")
    if first == 'q':
        break
    last = input("Please give me last name: ")
    if last == 'q':
        break

    formated_name = get_fomanted_name(first, last)
    print(f"\nNeatly formated name: {formated_name}")

