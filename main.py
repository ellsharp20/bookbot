def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def word_count(text_in):
    return len(text_in.split())

def char_count(text_in):
    char_counts = {}
    lowered_text = text_in.lower()
    word_list = lowered_text.split()
    no_spaces_text = "".join(word_list)

    for char in no_spaces_text:
        if char in char_counts.keys():
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts




book_text = main("books/frankenstein.txt")

print (word_count(book_text))

print(char_count(book_text))


