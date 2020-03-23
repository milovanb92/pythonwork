filename = 'text_files/learning_python.txt'

with open(filename) as file_object:
    print(file_object.read())

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.replace('Python', 'C').strip())