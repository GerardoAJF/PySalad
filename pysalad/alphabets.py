alphabets = dict()

def add_alphabet(name: str, alphabet, common_letters):
    """
    Add a new alphabet to the alphabets dictionary.
    You need to enter a list of all the letters of the alphabet and their variations, plus a list of the same but sorted by popularity.
    
    Example:
    name: "sw"
    alphabet: [("a", "A"), ("b", "B"), ...]
    common_letters: [("e", "E"), ("a", "A"), ...]
    """

    alphabet_letters = tuple(letter for letters in alphabet for letter in letters)

    alphabet_values = tuple(enumerate(alphabet))

    alphabet_letter_to_num = dict()
    alphabet_num_to_letter = dict()

    for num, letters in alphabet_values:
        for letter_num, letter in enumerate(letters):
            alphabet_letter_to_num[letter] = (num + 1, letter_num)
            alphabet_num_to_letter[(num + 1, letter_num)] = letter

    alphabets[name] = {
        "alphabet": alphabet,
        "len": len(alphabet),
        "letters": alphabet_letters,
        "letter_to_num": alphabet_letter_to_num,
        "num_to_letter": alphabet_num_to_letter,
        "common_letters": common_letters,
    }

# ***********************************************************************************

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

en_common_letters = (
    ("e", "E"), 
    ("t", "T"), 
    ("a", "A"), 
    ("o", "O"), 
    ("i", "I"),
    ("n", "N"),
    ("s", "S"),
    ("r", "R"),
    ("h", "H"),
    ("l", "L"),
    ("d", "D"),
    ("c", "C"),
    ("u", "U"),
    ("m", "M"),
    ("f", "F"),
    ("p", "P"),
    ("g", "G"),
    ("w", "W"),
    ("y", "Y"),
    ("b", "B"),
    ("v", "V"),
    ("k", "K"),
    ("x", "X"),
    ("j", "J"),
    ("q", "Q"),
    ("z", "Z")
)

add_alphabet("en", en_alphabet, en_common_letters)

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
    ("z", "Z")
)

es_common_letters = (
    ("e", "E", "é", "É"),
    ("a", "A", "á", "Á"),
    ("o", "O", "ó", "Ó"),
    ("s", "S"),
    ("r", "R"),
    ("n", "N"),
    ("i", "I", "í", "Í"),
    ("d", "D"),
    ("l", "L"),
    ("c", "C"),
    ("t", "T"),
    ("n", "N"),
    ("u", "U", "u", "Ú"),
    ("m", "M"),
    ("p", "P"),
    ("b", "B"),
    ("g", "G"),
    ("y", "Y"),
    ("v", "V"),
    ("q", "Q"),
    ("h", "H"),
    ("f", "F"),
    ("z", "Z"),
    ("j", "J"),
    ("ñ", "Ñ"),
    ("x", "X"),
    ("w", "W"),
    ("k", "K")
)

add_alphabet("es", es_alphabet, es_common_letters)
