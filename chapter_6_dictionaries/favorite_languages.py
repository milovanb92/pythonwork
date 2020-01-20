# dictionary structure:  name_of_dict = {'key': 'value', 'key2': 'value2'}

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"\nSarah's favorite language is {language}")


# items() method return all key-value pairs
for name, language in favorite_languages.items():
    print(f"{name.title()} favorite language is {language.title()}")

# keys() method return only keys from dictionary - default behavior of for loop 
for name in favorite_languages.keys():
    print(name.title())
# do the same thing:
for name in favorite_languages:
    print(name.title())

firends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in firends:
        # define variable language with value of name key mention in friends list
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take out the poll!")

# sort keys by alphabetic order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


# for loop through dictionary with values() method to return values of keys
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# set() print all values from dictionary without repeat
print("\nThe following languages without repeat:")
for language in set(favorite_languages.values()):
    print(language.title())