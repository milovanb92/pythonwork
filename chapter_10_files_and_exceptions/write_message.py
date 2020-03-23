filename = 'text_files/programming.txt'

# write mode 
# with open(filename, 'w') as file_object:
#     file_object.write("I love programming.\n")
#     file_object.write("Nema novih linija. \n")

# append mode
with open(filename, 'a') as file_object:
    file_object.write("Dodajemo nove linije. \n")
    file_object.write("Ne brisemo prethodne. \n")