from typing import TypedDict

class CharacterEntry(TypedDict):
    char: str
    count: int

CharacterList = list[CharacterEntry]
CharacterDict = dict[str, int]

def number_of_words(text: str) -> int:
    words = text.split()

    return len(words)

def character_occurrence(text: str) -> CharacterDict:
    characters: CharacterDict = {}

    for character in text.lower():
        characters[character] = characters.get(character, 0) + 1

    return characters

def alphabet_character_ranking(char_occurrence: CharacterDict) -> CharacterList:
    alphabet_list: CharacterList = [
        {"char": char, "count": count}
        for char, count in char_occurrence.items() if char.isalpha()
    ]

    alphabet_list.sort(reverse=True, key=lambda entry: entry["count"])

    return alphabet_list