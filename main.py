import sys
from stats import book_word_count
from stats import count_chars
from stats import sorted_list


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = book_word_count(sys.argv[1])
    char_count = count_chars(sys.argv[1])
    sorted_result = sorted_list(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_result:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")


if __name__ == "__main__":
    main()

