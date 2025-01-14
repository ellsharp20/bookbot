def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def count_words(text_in):
    return len(text_in.split())

def count_chars(text_in):
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

word_count = count_words(book_text)

char_dictionary = count_chars(book_text)

