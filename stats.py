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

def sort_by_occurence(some_dictionary):
    sorted_list = []
    
    for key, value in some_dictionary.items():
        sorted_list.append({"char": key, "num": value})
    def sort_on(item):
        return item["num"]
    sorted_list.sort(reverse=True, key=sort_on)   
    return sorted_list    
        
    
    
        