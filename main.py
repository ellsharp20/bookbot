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

def summarize_book_values(word_count, char_count):
    print(f"--- Begin report on  {doc_path} ---")
    print(f"{word_count} words found in this document")
    
    for char in char_count:
        print(f"The {char} character was found {char_count[char]} times")

    print("--- End Report ---")


doc_path = "books/frankenstein.txt"

book_text = main(doc_path)

word_count = count_words(book_text)

char_dictionary = count_chars(book_text)

summarize_book_values(word_count,char_dictionary)

