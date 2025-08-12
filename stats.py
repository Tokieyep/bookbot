def get_book_text(book_path):

    words_counter = 0

    with open(book_path) as file:
        content = file.read()
    
    words = content.split()

    print("Found", len(words), "total words")


    pass


def get_char_count(book_path):

    char_count = {}

    with open(book_path) as fi:


        for char in fi:
            for ch in char.lower():
                char_count[ch] = char_count.get(ch, 0) + 1
                
    #print(char_count)

    char_list = []
    for char, qty in char_count.items():
        if char.isalpha():
            char_list.append({char: qty})

    char_list.sort(key = lambda item: list(item.values())[0], reverse=True)

    for char in char_list:
        for chars, count in char.items():

            print(f'{chars}: {count}')



    pass


def reportEnd():




    pass