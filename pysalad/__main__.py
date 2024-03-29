import io

from pysalad import alphabets
from pysalad import code_text, decode_text

from pysalad.cesar_coder import create_code
from pysalad.cesar_decoder import get_number_codes
from pysalad.user import select_alphabet, get_file, save_file

def cesar_coder():
    alphabet = alphabets[select_alphabet()]

    code = create_code(alphabet)

    text = get_file()
    coded_text = code_text(code, text, alphabet)
    print(coded_text, "\n")

    save_file(coded_text)


def cesar_decoder():
    alphabet = alphabets[select_alphabet()]

    coded_text = get_file()

    number_codes = get_number_codes()

    text = io.StringIO()
    for decoded_text, code in decode_text(coded_text, alphabet, number_codes): 
        text.write(f"Trying Code: {code}---------------------\n")
        text.write(f"{decoded_text}\n\n")
    print(text.getvalue(), end="")

    save_file(text.getvalue())

if __name__ == "__main__":
    while True:
        print("Select an option: ")
        print("1. Cesar Coder")
        print("2. Cesar Decoder")
        print("3. Exit")

        option = input(">>")
        if option not in ["1", "2", "3"]:
            print("Enter a valid option\n")
            continue

        print()
        if option == "1":
            cesar_coder()
            continue

        if option == "2":
            cesar_decoder()
            continue

        if option == "3":
            break
