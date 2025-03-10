def get_num_words(file_contents):
    return len(file_contents.split())

def character_counter(file_contents):
    letter_dictionary = {}
    for i in file_contents:
        char = i.lower()
        if char in letter_dictionary:
            letter_dictionary[char] += 1
        else:
            letter_dictionary[char] = 1
    return letter_dictionary    


def sort_on(dict):
    return dict["count"]

def sort_character_count(char_count):
    sorted_characters = [
        {"character": ch, "count": count}
        for ch, count in char_count.items()
        if ch.isalpha()
    ]
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters
