import sys

from stats import get_book_text, get_char_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    char_count = get_char_count(book_path)

    
    
    return text, char_count

main()
