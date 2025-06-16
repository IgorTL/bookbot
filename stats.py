def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def book_word_count(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
        words = text.split()        
        return len(words)
    
def count_chars(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
        text = text.lower()
        char_count = dict()
        for char in text:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        return char_count
    
def sorted_list(char_count):
    char_list = []
    for char in char_count:
        char_list.append({"char": char, "num":char_count[char]})
    def sort_on(dict):
        return dict["num"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list