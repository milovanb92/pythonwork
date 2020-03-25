print("Please enter two numbers to add them together.")
print("Enter 'q' to quit.")

while True:
    first = input("Enter first number: ")
    if first == 'q':
        break
    second = input("Enter second number: ")
    if second == 'q':
        break
    try:
        result = int(first) + int(second)
    except ValueError:
        print("Unesi broj ne slovo!")
    else:
        print(result)
