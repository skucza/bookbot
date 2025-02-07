from typing import TypedDict


class CharacterEntry(TypedDict):
    char: str
    count: int


CharacterList = list[CharacterEntry]
CharacterDict = dict[str, int]


def main():
    book_path = "books/frankenstein.txt"

    with open(book_path, "r") as file:
        file_contents = file.read()
        word_count = number_of_words(file_contents)
        char_dictionary = number_of_characters(file_contents)
        alphabet_count = to_sorted_alphabet_list(char_dictionary)

        report(book_path, word_count, alphabet_count)


def number_of_words(text: str) -> int:
    words = text.split()

    return len(words)


def number_of_characters(text: str) -> CharacterDict:
    characters = {}
    lowercase_text = text.lower()

    for character in lowercase_text:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1

    return characters


def to_sorted_alphabet_list(characters_dict: CharacterDict) -> CharacterList:
    alphabet_list = []

    for entry in characters_dict:
        if entry.isalpha():
            alphabet_list.append({"char": entry, "count": characters_dict[entry]})

    def sort_on(character_entry):
        return character_entry["count"]

    alphabet_list.sort(reverse=True, key=sort_on)

    return alphabet_list


def report(filename: str, word_count: int, character_list: CharacterList):
    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the document")
    print()

    for entry in character_list:
        print(f"The '{entry['char']}' character was found {entry['count']}")

    print("--- End report ---")


if __name__ == "__main__":
    main()
