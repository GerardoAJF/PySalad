import io

from pysalad.alphabets import alphabets
from pysalad.utilities import read_file, write_file

def select_alphabet() -> str:
    """
    Provide the user with the alphabet they want to use.
    """

    alphabet_options = tuple(alphabets.keys())

    print("Select the alphabet you want to use: ")
    print(f"The options are: {alphabet_options}")

    while True:
        alphabet_selected = input(">>")

        if alphabet_selected in alphabet_options:
            break

        print("Enter a valid alphabet\n")

    print()
    return alphabet_selected


def get_file() -> str:
    """
    Provide the user with the option to specify the file that contains the text. If it is not given, then prompt the user to input the text directly.
    """

    print("Read a file?: ")

    file = yes_or_no_answer()

    if file:
        print("Enter the name of the file: ")
        file_name = input(">>")
        text = read_file(file_name)
    else:
        print("Enter the text: ")
        text = get_text()

    print()
    return text


def get_text() -> str:
    """
    Allow the user to enter multiple lines of text from the terminal.
    """

    text = io.StringIO()

    while True:
        inputs = input(">>")
        if not inputs:
            break

        text.write(f"{inputs}\n")

    return text.getvalue()


def save_file(text: str) -> None:
    """
    Prompt the user to specify a file to save the text.
    """

    print("Save the text in a file?:")

    save = yes_or_no_answer()

    if save:
        print("Enter the name of the new file: ")
        file_name = input(">>")

        if not file_name.endswith(".txt"):
            file_name = file_name + ".txt"

        write_file(file_name, text)
    print()


def yes_or_no_answer() -> bool:
    """
    Allow the user to choose between Yes or No, only those options.
    """

    print("Options: (Y/N)")
    while True:
        answer = input(">>")
        if answer in ("Y", "y", "N", "n"):
            break

        print("Enter a valid answer\n")

    print()
    if answer in ("Y", "y"):
        return True
    return False
