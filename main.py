def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text=text)
    num_characters = get_num_characters(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")

    for item in get_num_letters_desc(count_of_words=num_characters):
        print(f"The '{item[1]}' character was found {item[0]} times")


def get_num_letters_desc(count_of_words: dict[str, int]) -> list[(int, str)]:
    list_of_letters = []
    for letter in count_of_words:
        if letter.isalpha():
            list_of_letters.append((count_of_words[letter], letter))
    list_of_letters.sort(reverse=True)
    return list_of_letters


def get_num_words(text: str) -> int:
    return len(text.split())


def get_num_characters(text: str) -> dict[str, int]:
    count_letters = {}
    for letter in text.lower():
        if letter in count_letters:
            count_letters[letter] += 1
        else:
            count_letters[letter] = 1
    return count_letters


def get_book_text(book_path: str) -> str:
    with open(book_path) as f:
        return f.read()


main()
