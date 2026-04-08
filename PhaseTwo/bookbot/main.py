def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book_content = get_book_text("/home/bones/projects/bookbot/books/frankenstein.txt")
    print(book_content)


main()
