import io
import typing as t

from pysalad.alphabets import alphabets
from pysalad.utilities import count_letters
from pysalad.user import select_alphabet, get_file, save_file

def cesar_decode(text: str, alphabet: dict) -> t.List[int]:
    text_encode = remove_special_characters(text, alphabet)
    codes = list()

    commons_letter = count_letters(text_encode)
    common_letter_num = alphabet["letter_to_num"][max(commons_letter, key=commons_letter.get)]

    for al_common_letter in alphabet["common_letters"]:
        al_common_letter_num = alphabet["letter_to_num"][al_common_letter[0]]

        code = common_letter_num[0] - al_common_letter_num[0]
        if code < 0:
            code = alphabet["len"] + code
        codes.append(code)

    return codes


def remove_special_characters(text: str, alphabet: dict) -> str:
    format_text = io.StringIO()
    
    for letter in text:
        if letter not in alphabet["letters"]:
            continue

        format_text.write(letter)
    
    return format_text.getvalue()


def decode_text(text: str, alphabet: dict) -> t.List[t.Tuple[str, int]]:
    decoded_texts = list()

    codes = cesar_decode(text, alphabet)

    for code in codes:
        decoded_text = io.StringIO()
        for letter in text:
            if letter not in alphabet["letters"]:
                decoded_text.write(letter)
                continue

            letter_num = alphabet["letter_to_num"][letter]
            new_letter_num = letter_num[0] - code

            if new_letter_num <= 0:
                letter = alphabet["num_to_letter"][(alphabet["len"] + new_letter_num), letter_num[1]]
            else:
                letter = alphabet["num_to_letter"][(new_letter_num, letter_num[1])]

            decoded_text.write(letter)

        decoded_texts.append((decoded_text.getvalue(), code))
    return decoded_texts


if __name__ == "__main__":
    alphabet = alphabets[select_alphabet()]

    coded_text = get_file()

    text = io.StringIO()
    for decoded_text, code in decode_text(coded_text, alphabet): 
        text.write(f"Trying Code: {code}---------------------\n")
        text.write(f"{decoded_text}\n\n")
    print(text.getvalue(), end="")

    save_file(text.getvalue())
