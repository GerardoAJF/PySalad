import io
import typing as t

import utilities as u
import user as us
import alphabets as al

def cesar_decode(text: str, alphabet: dict) -> t.List[int]:
    text_encode = u.format_text(text)
    codes = list()

    commons_letter = u.count_letters(text_encode)
    common_letter_num = alphabet["letter_to_num"][max(commons_letter, key=commons_letter.get)]

    for al_common_letter in alphabet["common_letters"]:
        al_common_letter_num = alphabet["letter_to_num"][al_common_letter[0]]

        code = common_letter_num[0] - al_common_letter_num[0]
        if code < 0:
            code = alphabet["len"] + code
        codes.append(code)

    return codes


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
    alphabet = al.alphabets[us.select_alphabet()]
    
    file = input("\nEnter the name file:\n")

    text = ""
    for decoded_text, code in decode_text(u.read_file(file), alphabet):        
        text += f"\nTrying Code: {code}---------------------"
        text += f"\n{decoded_text}"
        text += "\n"

    print(text)

    u.write_file(f"decoded_{file}", text)
