import random
import io

import utilities as u
import alphabets as al

def code_text(code: int, text: str) -> str:
    text = text.lower() #TODO: to program only works in lowercase, not in uppercase
    coded_text = io.StringIO()

    len_alphabet = len(al.es_alphabet)

    for letter in text:
        if letter not in al.es_alphabet:
            coded_text.write(letter)
            continue

        coded_text.write(cesar_cipher(letter, code, len_alphabet))

    return coded_text.getvalue()


def cesar_cipher(letter: str, code: int, len_alphabet: int) -> str:
    letter_num = al.es_alphabet_letter_to_num[letter]
    new_letter_num = (letter_num + code) % len_alphabet

    if new_letter_num == 0:
        return al.es_alphabet_num_to_letter[len_alphabet]

    return al.es_alphabet_num_to_letter[new_letter_num]


if __name__ == "__main__":
    code = random.randint(0, len(al.es_alphabet) - 1)
    print(f"-------CODE: {code}------- ")
    
    file = input("\nEnter the name file:\n")
    coded_text = code_text(code, u.read_file(file))
    print(coded_text)
    
    while True:
        save = input("Do you want save the text in a file? (Y/N) ")
        if save in ("Y", "y", "N", "n"):
            break
        print("Enter a valid answer")
    
    if save in ("Y", "y"):
        u.write_file(f"coded_{file}", coded_text)
