import utilities as u
import alphabets as al

def calculate_steps(text: str) -> list:
    text = u.format_text(text)
    steps = list()

    commons_letter = u.count_letters(text)
    common_letter = max(commons_letter, key=commons_letter.get)

    for al_common_letter in al.es_common_letters:
        step = al.es_alphabet_letter_to_num[common_letter] - al.es_alphabet_letter_to_num[al_common_letter]
        
        if step < 0:
            step = (len(al.es_alphabet) - al.es_alphabet_letter_to_num[al_common_letter]) + al.es_alphabet_letter_to_num[common_letter]

        steps.append(step)
    return steps


def decode_text(text: str):
    text = text.lower()
    decoded_texts = list()

    steps = calculate_steps(text)
    for step in steps:
        new_text = ""

        for letter in text:
            if letter in al.es_alphabet:
                letter_num = al.es_alphabet_letter_to_num[letter]
                new_letter_num = letter_num - step

                if new_letter_num <= 0:
                    letter = al.es_alphabet_num_to_letter[len(al.es_alphabet) + new_letter_num]
                else:
                    letter = al.es_alphabet_num_to_letter[new_letter_num]

            new_text += letter

        decoded_texts.append(new_text)

    return zip(decoded_texts, steps)


if __name__ == "__main__":
    file = input("\nEnter the name file:\n")

    text = ""
    for decoded_text, code in decode_text(u.read_file(file)):        
        text += f"\nTrying Code: {code}---------------------"
        text += f"\n{decoded_text}"
        text += "\n"

    print(text)

    u.write_file(f"decoded_{file}", text)
