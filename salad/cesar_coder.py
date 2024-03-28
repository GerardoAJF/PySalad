import random
import io

from salad.alphabets import alphabets
from salad.user import yes_or_no_answer, select_alphabet, get_file, save_file

def code_text(code: int, text: str, alphabet: dict) -> str:
    coded_text = io.StringIO()

    for letter in text:
        if letter not in alphabet["letters"]:
            coded_text.write(letter)
            continue

        coded_text.write(cesar_cipher(letter, code, alphabet))

    return coded_text.getvalue()


def cesar_cipher(letter: str, code: int, alphabet: dict) -> str:
    letter_num = alphabet["letter_to_num"][letter]
    new_letter_num = (letter_num[0] + code) % alphabet["len"]

    if new_letter_num == 0:
        return alphabet["num_to_letter"][(alphabet["len"], letter_num[1] % 2)]

    return alphabet["num_to_letter"][(new_letter_num, letter_num[1] % 2)]


def create_code(alphabet) -> int:
    print("Create a random code?:")
    random_code = yes_or_no_answer()

    if random_code:
        code = random.randint(1, alphabet["len"]-1)
    else:
        print("Enter a code:")

        while True:
            code = input(">>")
            if code.isnumeric() and int(code) <= (alphabet["len"]-1) and int(code) >= 1:
                code = int(code)
                break

            print("Enter a valid code\n")

    print(f"The CODE is: {code}")
    print()
    return code


if __name__ == "__main__":
    alphabet = alphabets[select_alphabet()]

    code = create_code(alphabet)
    print(f"-------CODE: {code}------- ")

    text = get_file()
    coded_text = code_text(code, text, alphabet)
    print(coded_text, "\n")

    save_file(coded_text)
