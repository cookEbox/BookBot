import string

def sort_on(dict):
    return dict["count"]

def list_of_dicts(a_dict):
    list_of_dicts = []
    for a in a_dict:
        list_of_dicts.append({"char" : a, "count" : a_dict[a]})
    return (list_of_dicts)

def create_dictionary():
    character_dict = {}
    alphabet = string.ascii_lowercase
    for char in alphabet:
        character_dict[char] = 0
    return character_dict

def number_chars_dict(text):
    character_dict = create_dictionary()
    for char in text:
        if char in character_dict:
            character_dict[char] += 1
    return character_dict

def print_report(path, a_list_dict, count):
    first_line = "--- Begin report of " + path + " ---\n"
    second_line = str(count) + " words found in the document\n\n"
    main_body = ""
    for a in a_list_dict:
        main_body += "The " + "\'" + a["char"] + "\' " + "character was found " + str(a["count"]) + " times\n"
    end = "--- End report ---"
    print(first_line + second_line + main_body + end)

def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        frank = f.read()
        lower_case_frank = frank.lower()
        listed_chars = list_of_dicts(number_chars_dict(lower_case_frank))
        listed_chars.sort(reverse=True, key=sort_on)
        print_report(book_path, listed_chars, len(frank.split()))

main()
