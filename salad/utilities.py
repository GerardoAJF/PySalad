import typing as t

def read_file(file_name: str) -> str:
    text = str()

    with open(file_name, "r", encoding="utf-8") as file:
        for letter in file:
            text = text + letter

    return text


def write_file(file_name: str, text: str) -> None:
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(text)


def format_text(text: str) -> str:
    text = text.replace(" ", "").strip()
    return text


def count_letters(text: str) -> t.Dict[str, int]:
    letters = dict()
    
    for letter in text:
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1

    return letters
