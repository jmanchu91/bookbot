import sys

if len(sys.argv) < 2:
    print("Usage: python2 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]

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
    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    char_count = character_counter(book_text)
    sorted_count = sort_character_count(char_count)
    print("============ BOOKBOT ============ \nAnalyzing book found at", path, "...")
    print("----------- Word Count ----------")
    print("Found", num_words, "total words")
    print("--------- Character Count -------")
    for entry in sorted_count:
        print(f"{entry['character']}: {entry['count']}")
    
main()

