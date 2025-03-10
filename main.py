def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words

from stats import character_counter

from stats import sort_character_count

def main():
    num_words = 0
    char_count = {}
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    char_count = character_counter(book_text)
    sorted_count = sort_character_count(char_count)
    print("============ BOOKBOT ============"
    "Analyzing book found at books/frankestein.txt")
    print(num_words, "words found in the document")
    print(char_count)
    print(sorted_count)
    
main()

