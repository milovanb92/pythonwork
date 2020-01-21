favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

users = ['miki', 'sarah', 'kico', 'sasa', 'phil']
for user in users:
    if user in favorite_languages.keys():
        print(f"{user} thank you for taking the poll.")
    else:
        print(f"{user} please take the poll!")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print(f"\n{name.title()}'s favorite language are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")