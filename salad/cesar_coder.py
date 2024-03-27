import random
import io

import utilities as u
import user as us
import alphabets as al

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


if __name__ == "__main__":
    alphabet = al.alphabets[us.select_alphabet()]

    code = random.randint(0, alphabet["len"]-1)
    print(f"-------CODE: {code}------- ")

    file = input("\nEnter the name file:\n")
    coded_text = code_text(code, u.read_file(file), alphabet)
    print(coded_text)

    while True:
        save = input("Do you want save the text in a file? (Y/N) ")
        if save in ("Y", "y", "N", "n"):
            break
        print("Enter a valid answer")

    if save in ("Y", "y"):
        u.write_file(f"coded_{file}", coded_text)
