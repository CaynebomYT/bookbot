def get_word_count(some_text):
    num_words = 0
    some_text = some_text.split(None)
    for text in some_text:
        num_words += 1
    return num_words

def get_character_count(some_text):
    some_text = some_text.lower()
    character_count = {}
    for text in some_text:
        for character in text:
            if (character in character_count) == True:
                character_count[character] = character_count[character] + 1
            else:
                character_count[character] = 1
    return character_count
