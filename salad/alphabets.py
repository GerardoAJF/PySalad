en_alphabet = (
    ("a", "A"),
    ("b", "B"),
    ("c", "C"),
    ("d", "D"),
    ("e", "E"),
    ("f", "F"),
    ("g", "G"),
    ("h", "H"),
    ("i", "I"),
    ("j", "J"),
    ("k", "K"),
    ("l", "L"),
    ("m", "M"),
    ("n", "N"),
    ("o", "O"),
    ("p", "P"),
    ("q", "Q"),
    ("r", "R"),
    ("s", "S"),
    ("t", "T"),
    ("u", "U"),
    ("v", "V"),
    ("w", "W"),
    ("x", "X"),
    ("y", "Y"),
    ("z", "Z")
)

en_alphabet_letters = tuple(letter for letters in en_alphabet for letter in letters)

en_alphabet_values = tuple(enumerate(en_alphabet))

en_alphabet_letter_to_num = dict()
en_alphabet_num_to_letter = dict()

for num, letters in en_alphabet_values:
    for letter_num, letter in enumerate(letters):
        en_alphabet_letter_to_num[letter] = (num + 1, letter_num)
        en_alphabet_num_to_letter[(num + 1, letter_num)] = letter

en_common_letters = (
    ("e", "E"), 
    ("a", "A"), 
    ("r", "R"), 
    ("i", "I"), 
    ("o", "O")
)

# ***********************************************************************************

es_alphabet = (
    ("a", "A", "á", "Á"),
    ("b", "B"),
    ("c", "C"),
    ("d", "D"),
    ("e", "E", "é", "É"),
    ("f", "F"),
    ("g", "G"),
    ("h", "H"),
    ("i", "I", "í", "Í"),
    ("j", "J"),
    ("k", "K"),
    ("l", "L"),
    ("m", "M"),
    ("n", "N"),
    ("ñ", "Ñ"),
    ("o", "O", "ó", "Ó"),
    ("p", "P"),
    ("q", "Q"),
    ("r", "R"),
    ("s", "S"),
    ("t", "T"),
    ("u", "U", "ú", "Ú", "ü", "Ü"),
    ("v", "V"),
    ("w", "W"),
    ("x", "X"),
    ("y", "Y"),
    ("z", "Z"),
)
es_alphabet_letters = tuple(letter for letters in es_alphabet for letter in letters)

es_alphabet_values = tuple(enumerate(es_alphabet))

es_alphabet_letter_to_num = dict()
es_alphabet_num_to_letter = dict()

for num, letters in es_alphabet_values:
    for letter_num, letter in enumerate(letters):
        es_alphabet_letter_to_num[letter] = (num + 1, letter_num)
        es_alphabet_num_to_letter[(num + 1, letter_num)] = letter

es_common_letters = (
    ("e", "E", "é", "É"),
    ("a", "A", "á", "Á"),
    ("o", "O", "ó", "Ó"),
    ("s", "S"),
    ("r", "R")
)

# ***********************************************************************************

alphabets = {
    "en": {
        "alphabet": en_alphabet,
        "len": len(en_alphabet),
        "letters": en_alphabet_letters,
        "letter_to_num": en_alphabet_letter_to_num,
        "num_to_letter": en_alphabet_num_to_letter,
        "common_letters": en_common_letters
    },
    "es": {
        "alphabet": es_alphabet,
        "len": len(es_alphabet),
        "letters": es_alphabet_letters,
        "letter_to_num": es_alphabet_letter_to_num,
        "num_to_letter": es_alphabet_num_to_letter,
        "common_letters": es_common_letters
    }
}

