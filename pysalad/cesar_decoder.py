import io
import typing as t

from pysalad.utilities import count_letters
from pysalad.user import yes_or_no_answer


def cesar_decode(text: str, alphabet: dict, number_codes: int = 5) -> t.List[int]:
    """
    Take the text, and assuming that the most common letter is one of the most common letters in the language, calculate a list with the numbers of specified possible codes.
    """

    text_encode = remove_special_characters(text, alphabet)
    codes = list()

    commons_letter = count_letters(text_encode)
    common_letter_num = alphabet["letter_to_num"][max(commons_letter, key=commons_letter.get)]

    for al_common_letter in alphabet["common_letters"][:number_codes]:
        al_common_letter_num = alphabet["letter_to_num"][al_common_letter[0]]

        code = common_letter_num[0] - al_common_letter_num[0]
        if code < 0:
            code = alphabet["len"] + code
        codes.append(code)

    return codes


def remove_special_characters(text: str, alphabet: dict) -> str:
    """
    Remove all the characters from the text that are not in the alphabet (only letters).
    """

    format_text = io.StringIO()

    for letter in text:
        if letter not in alphabet["letters"]:
            continue

        format_text.write(letter)

    return format_text.getvalue()


def decode_text(
    text: str,
    alphabet: dict,
    number_codes: int = 5,
) -> t.List[t.Tuple[str, int]]:
    """
    Try the specified number of possible codes on the encoded text, and return the list of results along with the corresponding trial code.
    """

    decoded_texts = list()

    codes = cesar_decode(text, alphabet, number_codes)

    for code in codes:
        decoded_text = io.StringIO()
        for letter in text:
            if letter not in alphabet["letters"]:
                decoded_text.write(letter)
                continue

            letter_num = alphabet["letter_to_num"][letter]
            new_letter_num = letter_num[0] - code

            if new_letter_num <= 0:
                letter = alphabet["num_to_letter"][
                    (alphabet["len"] + new_letter_num), letter_num[1]
                ]
            else:
                letter = alphabet["num_to_letter"][(new_letter_num, letter_num[1])]

            decoded_text.write(letter)

        decoded_texts.append((decoded_text.getvalue(), code))
    return decoded_texts


def get_number_codes() -> int:
    """
    Provide the user with the option to specify the number of possible codes.
    """
    
    print("Do you want specify the number of codes?: ")
    specify_codes = yes_or_no_answer()
    
    number_codes = 5
    
    if specify_codes:
        print("Enter the number of codes: ")
        
        while True:
            number_codes = input(">>")
            if number_codes.isnumeric():
                number_codes = int(number_codes)
                break
            
            print("Enter a valid number of codes\n")
    
    print()
    return number_codes