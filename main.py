def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print_report(book_path, num_words, text)

def print_report(book_path, num_words, text):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    sorted_list = sort_dict(count_letters(text))
    for item in sorted_list:
        print(f"The '{item["ltr"]}' character was found {item["count"]} times")
    print("--- End report ---")


def sort_on(d):
    return d["count"]

def sort_dict(dict):
    sorted_letters = []
    for k, v in dict.items():
        if k.isalpha():
            sorted_letters.append({"ltr": k, "count": v})
    sorted_letters.sort(reverse=True, key=sort_on)
    return sorted_letters

def count_letters(text):
    letters = {}
    for char in text:
        lchar = char.lower()
        if lchar in letters:
            letters[lchar] += 1
        else:
            letters[lchar] = 1
    return letters


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
