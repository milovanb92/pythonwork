filenames = ['cats.txt', 'dogs.txt']

for name in filenames:
    try:
        with open(name, encoding='utf-8') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        # print("Fajl ne postoji!")
        pass