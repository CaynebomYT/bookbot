from stats import get_word_count
from stats import get_character_count

def get_books_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_books_text("./books/frankenstein.txt")
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    


main()