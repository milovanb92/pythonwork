filename = 'text_files/pi_milion_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

# print(f"{pi_string[:52]}")
# print(len(pi_string))

birthday = input("Enter you birthday in form ddmmyy: ")
if birthday in pi_string:
    print("Your birthday apears in the first million digits of pi!")
else:
    print("Your birthday DOES NOT apears in the first million digits of pi!")