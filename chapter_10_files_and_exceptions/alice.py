def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()

    except FileNotFoundError:
        # print(f"Sorry the file {filename} does not exist!")
        pass
    else:
        # count the aproximately number of words in a file
        # words = content.split()
        # num_words = len(words)
        # print(f"The file {filename} has about {num_words} words.")
        print("The word apears: ")
        print(content.count('them'))


filename = ['konj', 'text_files/alice.txt', 'text_files/sidharta.txt', 'text_files/mobydick.txt']
for file in filename:
    count_words(file)