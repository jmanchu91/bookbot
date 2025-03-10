def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words

def main():
    num_words = 0
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)

    print(num_words, "words found in the document")

main()

