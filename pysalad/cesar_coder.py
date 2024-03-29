import random
import io

from pysalad.user import yes_or_no_answer

def code_text(code: int, text: str, alphabet: dict) -> str:
    """
    Move each letter of the text in the alphabet by the number of times specified in the code. 
    Letters that are not in the alphabet are not encoded.
    """

    coded_text = io.StringIO()

    for letter in text:
        if letter not in alphabet["letters"]:
            coded_text.write(letter)
            continue

        coded_text.write(cesar_cipher(letter, code, alphabet))

    return coded_text.getvalue()


def cesar_cipher(letter: str, code: int, alphabet: dict) -> str:
    """
    Move one letter in the alphabet by the number of times specified in the code.
    Only works with letters in the alphabet.
    """

    letter_num = alphabet["letter_to_num"][letter]
    new_letter_num = (letter_num[0] + code) % alphabet["len"]

    if new_letter_num == 0:
        return alphabet["num_to_letter"][(alphabet["len"], letter_num[1] % 2)]

    return alphabet["num_to_letter"][(new_letter_num, letter_num[1] % 2)]


def create_code(alphabet) -> int:
    """
    Provide the user with a code; if one is not given, then generate a random one.
    """

    print("Create a random code?:")
    random_code = yes_or_no_answer()

    code = random.randint(1, alphabet["len"]-1)
    
    if not random_code:
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
