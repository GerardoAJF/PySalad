<p align="center">
    <img src="https://github.com/GerardoAJF/PySalad/blob/main/assets/imgs/logo.svg" width="300px", alt="PySalad Logo">
</p>

<p align="center">
    <img alt="Static Badge" src="https://img.shields.io/badge/Status-Beta-orange?style=for-the-badge">
    <img alt="Static Badge" src="https://img.shields.io/badge/Latest Stable Version-In Process-orange?style=for-the-badge">
    <img alt="Static Badge" src="https://img.shields.io/badge/Latest Version-0.1-blue?style=for-the-badge">
    <img alt="Static Badge" src="https://img.shields.io/badge/Package Version-0.1-purple?style=for-the-badge">
    <img alt="Static Badge" src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge&link=https%3A%2F%2Fopensource.org%2Flicense%2Fmit">
</p>

Pysalad is a package written entirely in native Python used to encode and decode text using the Caesar cipher.

It is a fairly small project that advocates simplicity, so it is easy to integrate into any project, despite this it has some potential to be able to work with multiple alphabets.

It has a cli interface, so the user can use it as a simple terminal tool if desired.

## Install

Pysalad is my first package, that's why it is hosted in TestPyPi instead of just PyPi.

1 - Make sure you have both python3 and pip installed.
2 - Execute the following command using pip 3

```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ pysalad
```

## Getting started

### Code and Decode text

The two main functions of the package are **code_text()** and **decode_text()** which encompass the encoding and decoding logic.

#### Example of use

##### Code text

The function moves each of the letters of the text in the alphabet the number of times the code specifies.

```python
import pysalad as salad

text = "This is a text that I want to encode!!"
coded_text = salad.code_text(2, text, salad.alphabets["en"])
print(coded_text) # Vjku ku c vgzv vjcv K ycpv vq gpeqfg!!
```

Or, if you want to create a pseudo-random code

```python
import pysalad as salad
import random

text = "This is a text that I want to encode!!"
code = random.randint(1, salad.alphabets["en"]["len"])
coded_text = salad.code_text(code, text, salad.alphabets["en"])
print(code)  # 24
print(coded_text)  # Rfgq gq y rcvr rfyr G uylr rm clambc!!
```

##### Decode text

The function counts which is the most repeated letter in the text, and assuming that this is one of the most repeated letters in the selected language, tests the most probable codes.

```python
import pysalad as salad

coded_text = "Ftue ue m fqjf ftmf U imzf fa qzoapq!!"
decoded_texts = salad.decode_text(coded_text, salad.alphabets["en"], 3)
for decoded_text, tried_code in decoded_texts:
    print(decoded_text, "---", tried_code)

    # Estd td l epie esle T hlye ez pynzop!! --- 1
    # This is a text that I want to encode!! --- 12
    # Aopz pz h alea aoha P dhua av lujvkl!! --- 5
```

### CLI

Pysalad has a simple console line interface so you can use it from the terminal.

<p>
    <img src="https://github.com/GerardoAJF/PySalad/blob/main/assets/imgs/CLI.gif" alt="PySalad CLI">
</p>

You can access it just by running `pysalad`.

## Documentation

### More functions

**count_letters()** counts how many times all letters in a text are repeated, regardless of whether they are in upper or lower case.

```python
text = "Hello world!, how are you?"
print(salad.count_letters(text))
# {'h': 2, 'e': 2, 'l': 3, 'o': 4, ' ': 4, 'w': 2, 'r': 2, 'd': 1, '!': 1, ',': 1, 'a': 1, 'y': 1, 'u': 1, '?': 1}
```

**remove_special_characters()** removes all characters not found in the given alphabet.

```python

text = "Mañana iré a tomar café..."
print(salad.remove_special_characters(text, salad.alphabets["en"]))  # Maanairatomarcaf
```

**cesar_cipher()** encrypts the letter using the cesar cipher, only works with letters that are in the alphabet.

```python
print(salad.cesar_cipher("z", 1, salad.alphabets["en"]))  # a
print(salad.cesar_cipher("A", 1, salad.alphabets["en"]))  # B
print(salad.cesar_cipher("é", 2, salad.alphabets["es"]))  # g
```

**cesar_decode()** assuming that the most common letter is one of the most common letters of the alphabet, return the most likely codes (you can specify the number).

```python
text = "Hello world!, this a text that I want to encode!"
coded_text = salad.code_text(1, text, salad.alphabets["en"])
print(coded_text)  # Ifmmp xpsme!, uijt b ufyu uibu J xbou up fodpef!

print(salad.cesar_decode(coded_text, salad.alphabets["en"]))  # [16, 1, 20, 6, 12]
```

**read_file** and **write_file** return and save the text of a file respectively.

```python
text = "Hello world from pysalad"
salad.write_file("text.txt", text)

recovered_text = salad.read_file("text.txt")
print(recovered_text)  # Hello world from pysalad
```

### Alphabets

As mentioned above Pysalad is able to work with the alphabets of multiple languages by representing them as dictionaries of the following structure:

```python
"en": {
        "alphabet": en_alphabet,
        "len": len(en_alphabet),
        "letters": en_alphabet_letters,
        "letter_to_num": en_alphabet_letter_to_num,
        "num_to_letter": en_alphabet_num_to_letter,
        "common_letters": en_common_letters
    }
```

At the same time all these are in the dictionary **alphabets**.

#### Add new alphabets

1 - First we must add all the letters of the alphabet in order and with their variant in capital letters.

```python
sw_alphabet = (
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
    ("r", "R"),
    ("s", "S"),
    ("t", "T"),
    ("u", "U"),
    ("v", "V"),
    ("w", "W"),
    ("x", "X"),
    ("y", "Y"),
    ("z", "Z"),
    ("å", "Å"),
    ("ä", "Ä"),
    ("ö", "Ö")
)
```

2 - We will do the same with the most common letters of this alphabet.

```python
sw_common_letters = (
    ("e", "E"),
    ("a", "A"),
    ("n", "N"),
    ("t", "T"),
    ("r", "R"),
    ("s", "S"),
    ("l", "L"),
    ("i", "I"),
    ("d", "D"),
    ("o", "O"),
    ("m", "M"),
    ("g", "G"),
    ("k", "K"),
    ("v", "V"),
    ("ä", "Ä"),
    ("h", "H"),
    ("f", "F"),
    ("u", "U"),
    ("p", "P"),
    ("å", "Å"),
    ("ö", "Ö"),
    ("b", "B"),
    ("c", "C"),
    ("j", "J"),
    ("y", "Y"),
    ("x", "X"),
    ("w", "W"),
    ("z", "Z")
)
```

3 - We can obtain the missing lists using the following code:

```python
sw_alphabet_letters = tuple(letter for letters in sw_alphabet for letter in letters)

sw_alphabet_values = tuple(enumerate(sw_alphabet))

sw_alphabet_letter_to_num = dict()
sw_alphabet_num_to_letter = dict()

for num, letters in sw_alphabet_values:
    for letter_num, letter in enumerate(letters):
        sw_alphabet_letter_to_num[letter] = (num + 1, letter_num)
        sw_alphabet_num_to_letter[(num + 1, letter_num)] = letter
```

4 - We can now add the alphabet to the dictionary of alphabets.

```python
salad.alphabets["sw"] = {
        "alphabet": sw_alphabet,
        "len": len(sw_alphabet),
        "letters": sw_alphabet_letters,
        "letter_to_num": sw_alphabet_letter_to_num,
        "num_to_letter": sw_alphabet_num_to_letter,
        "common_letters": sw_common_letters
    }
```

5 - We can test that it works correctly.

```python
text = "Jag älskar att gå längs älven på hösten."
code = 2
coded_text = salad.code_text(code, text, salad.alphabets["sw"])
print(coded_text)  # Lci anumct cvv iö napiu anxgp sö jbuvgp.

decoded_texts = salad.decode_text(coded_text, salad.alphabets["sw"])
for decoded_text, tried_code in decoded_texts:
    print(tried_code, "---", decoded_text)

    # 26 --- Nek cpwoev exx kb pcskw cpzis ub ldwxis.
    # 2 --- Jag älskar att gå längs älven på hösten.
    # 17 --- Xnu lzcynb ndd uk zläuc lzfsä ak vmcdsä.
    # 12 --- Ötz rbhatg tii zp brdzh rbkxd fp åshixd.
    # 14 --- Årx oöfäre rgg xn öobxf oöivb dn ypfgvb.
```

### Security

Cesar encryption itself is quite insecure, so it is not recommended to use it for confidential data of any kind.

## Contributing

Feel free to make suggestions, report bugs or modify the code base, when I can I will review them.

## License

The license of this project is the [MIT license](https://choosealicense.com/licenses/mit/), so use it as you want but don't forget to give the necessary credits.
