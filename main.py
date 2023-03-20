filename = "books/frankenstein.txt"

with open("books/frankenstein.txt", "r" ) as f:
    contents = f.read()

def word_count(string):
    count = [len(string.split())]
    return count

def letter_count(string):
    string_dict = {}
    string = string.lower()

    for i in range(0, len(string)):
        if string[i].isalpha():
            if string[i] not in string_dict:
                string_dict[string[i]] = 1
            else:
                string_dict[string[i]] += 1
    dict_back_to_list = list(string_dict.items())
    sorted_by_count = sorted(dict_back_to_list, key=lambda string: string[1], reverse=True)

    return sorted_by_count

def main(string_arr):
    print(f"-- Bookbot is working on {filename} --\n")
    print(f"There are {word_count(string_arr)} words in this book!\n")
    print(f"There are also the following counts of each letter: \n")
    letters_count = letter_count(string_arr)
    for key, value in letters_count:
        print(f"{key}: {value}")
    

main(contents)