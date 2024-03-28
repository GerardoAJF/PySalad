import io

from salad import alphabets
from salad import code_text, decode_text

from salad.cesar_coder import create_code
from salad.user import select_alphabet, get_file, save_file

def cesar_coder():
    alphabet = alphabets[select_alphabet()]

    code = create_code(alphabet)
    print(f"-------CODE: {code}------- ")

    text = get_file()
    coded_text = code_text(code, text, alphabet)
    print(coded_text, "\n")

    save_file(coded_text)


def cesar_decoder():
    alphabet = alphabets[select_alphabet()]

    coded_text = get_file()

    text = io.StringIO()
    for decoded_text, code in decode_text(coded_text, alphabet): 
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
