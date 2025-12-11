def sort_on(items):
    return items["num"]


def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
    return file_contents


def num_of_words_in_text(text):
    return len(text)

def get_words(text):
    all_the_words = text.split()
    return all_the_words

def num_of_chars(words):
    word_to_count = {}
    new_word_count = [] 
    for w in words:
        list_of_chars = list(w)
        for l in list_of_chars:
            ll = l.lower()
            if ll not in word_to_count:
                word_to_count[ll] = 1
            else:
                word_to_count[ll] += 1
    for index in word_to_count:
        new_word_count.append({"char": index, "num": word_to_count[index]})
    new_word_count.sort(reverse=True, key=sort_on)
    return new_word_count
