import io

import salad.utilities as u
import alphabets as al

def calculate_codes(text: str) -> list:
    text_encode = u.format_text(text)
    codes = list()

    len_alphabet = len(al.es_alphabet)

    commons_letter = u.count_letters(text_encode)
    common_letter_num = al.es_alphabet_letter_to_num[max(commons_letter, key=commons_letter.get)]

    for al_common_letter in al.es_common_letters:
        al_common_letter_num = al.es_alphabet_letter_to_num[al_common_letter]

        code = common_letter_num - al_common_letter_num
        if code < 0:
            code = len_alphabet + code
        codes.append(code)

    return codes


def decode_text(text: str):
    text_coded = text.lower()  # TODO: to program only works in lowercase, not in uppercase
    decoded_texts = list()

    len_alphabet = len(al.es_alphabet)

    codes = calculate_codes(text_coded)

    for code in codes:
        decoded_text = io.StringIO()
        for letter in text_coded:
            if letter not in al.es_alphabet:
                decoded_text.write(letter)
                continue

            letter_num = al.es_alphabet_letter_to_num[letter]
            new_letter_num = letter_num - code

            if new_letter_num <= 0:
                letter = al.es_alphabet_num_to_letter[len_alphabet + new_letter_num]
            else:
                letter = al.es_alphabet_num_to_letter[new_letter_num]

            decoded_text.write(letter)

        decoded_texts.append((decoded_text.getvalue(), code))
    return decoded_texts


if __name__ == "__main__":
    file = input("\nEnter the name file:\n")

    text = ""
    for decoded_text, code in decode_text(u.read_file(file)):        
        text += f"\nTrying Code: {code}---------------------"
        text += f"\n{decoded_text}"
        text += "\n"

    print(text)

    u.write_file(f"decoded_{file}", text)
