def sort_on(items):
    return items["num"]
def create_report(book_data):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_data['book_path']}...")
    print("----------- Word Count ----------")
    print(f"Found {book_data['word_count']} total words")
    print("--------- Character Count -------")
    for index in book_data["letter_data"]:
        print(f"{index['char']}: {index['num']}")
    print("============= END ===============")

