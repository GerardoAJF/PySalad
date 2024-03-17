import random

import utilities as u
import alphabets as al

def code_text(code: int, text: str) -> str:
    new_text = str()

    for letter in text:
        letter = letter.lower() #TODO: to program only works in lowercase, not in uppercase

        if letter in al.es_alphabet:
            letter_num = al.es_alphabet_letter_to_num[letter]
            new_letter_num = letter_num + code
            
            if (new_letter_num % len(al.es_alphabet)) == 0:
                letter = al.es_alphabet_num_to_letter[len(al.es_alphabet)]
            else:
                letter = al.es_alphabet_num_to_letter[new_letter_num % len(al.es_alphabet)]
        
        new_text += letter
        
    return new_text

if __name__ == "__main__":
    code = random.randint(0, len(al.es_alphabet) - 1)
    print(f"-------CODE: {code}------- ")
    
    file = input("\nEnter the name file:\n")
    coded_text = code_text(code, u.read_file(file))
    print(coded_text)
    
    while True:
        save = input("Do you want save the text in a file? (Y/N) ")
        if save in ["Y", "y", "N", "n"]:
            break
        print("Enter a valid answer")
    
    if save == "Y" or save == "y":
        u.write_file(f"coded_{file}", coded_text)
