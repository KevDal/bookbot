from stats import get_book_text, num_of_words_in_text, num_of_chars, get_words
from report import create_report
import sys
print(sys.argv)
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    book_text = get_book_text(path)
    words = get_words(book_text)
    number_of_words = num_of_words_in_text(words)
    letter_data = num_of_chars(words)
    book_data = {}
    book_data['book_path'] = path
    book_data['word_count'] = number_of_words
    book_data['letter_data'] = letter_data
    create_report(book_data)
    

main()
