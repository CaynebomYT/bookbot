from stats import get_word_count
from stats import get_character_count
from stats import sort_by_occurence
import sys

def get_books_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_books_text("./books/frankenstein.txt")
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    character_count = sort_by_occurence(character_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found", word_count, "total words")
    print("--------- Character Count -------")
    for character in character_count:
        is_letter = character["char"]
        if is_letter.isalpha() == True:
            print(f"{is_letter}:", character["num"])
    print("============= END ===============")
    



main()