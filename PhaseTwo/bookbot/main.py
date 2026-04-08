def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def text_to_string(text):
    split_text = len(text.split())
    return split_text


def main():
    book_content = get_book_text("/home/bones/projects/PythonBootcamp/PhaseTwo/bookbot/books/frankenstein.txt")
    word_count = text_to_string(book_content)
    print(f"Found {word_count} total words")


main()
