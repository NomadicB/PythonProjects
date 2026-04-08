import sys
from stats import text_to_string, text_to_count, sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_content = get_book_text(sys.argv[1])
    word_count = text_to_string(book_content)
    string_count = text_to_count(book_content)
    list_sorted = sorted_list(string_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in list_sorted:
        if not i["char"].isalpha():
            continue
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")


main()
