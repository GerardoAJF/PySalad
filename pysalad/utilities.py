import typing as t
import io

def read_file(file_name: str) -> str:
    """
    Read the text from the file.
    """

    text = io.StringIO()

    with open(file_name, "r", encoding="utf-8") as file:
        for letter in file:
            text.write(letter)

    return text.getvalue()


def write_file(file_name: str, text: str) -> None:
    """
    Save the text to the file.
    """

    with open(file_name, "w", encoding="utf-8") as file:
        file.write(text)


def count_letters(text: str) -> t.Dict[str, int]:
    """
    Count the number of letters and characters in a text.
    It is not case sensitive.
    """

    letters = dict()
    text = text.lower()

    for letter in text:
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1

    return letters
