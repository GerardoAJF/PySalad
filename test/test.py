import sys

sys.path.append("../salad")

from salad import alphabets
from salad import count_letters
from salad import cesar_cipher, code_text
from salad import remove_special_characters, cesar_decode, decode_text


def test_count_letters():
    text = "Hello WorLd"
    assert count_letters(text) == {'h': 1, 'e': 1, 'l': 3, 'o': 2, " ": 1, 'w': 1, 'r': 1, 'd': 1}


def test_cesar_cipher():
    code = 1
    assert cesar_cipher("n", code, alphabets["en"]) == "o"
    assert cesar_cipher("z", code, alphabets["en"]) == "a"
    assert cesar_cipher("A", code, alphabets["en"]) == "B"

    assert cesar_cipher("n", code, alphabets["es"]) == "ñ"
    assert cesar_cipher("z", code, alphabets["es"]) == "a"
    assert cesar_cipher("Á", code, alphabets["es"]) == "B"


def test_code_text():
    code = 3
    assert code_text(code, "Hello World", alphabets["en"]) == "Khoor Zruog"
    assert code_text(code, "Hello World", alphabets["es"]) == "Khññr Zruñg"


def test_remove_special_characters():
    text = "aeiou áéóíú abcd ññ!!"
    assert remove_special_characters(text, alphabets["en"]) == "aeiouabcd"
    assert remove_special_characters(text, alphabets["es"]) == "aeiouáéóíúabcdññ"


def test_cesar_decode():
    assert cesar_decode("Elephants remember every event easily.", alphabets["en"]) == [0, 4, 13, 22, 16, 11]
    assert cesar_decode("Los elefantes recuerdan eventos fácilmente.", alphabets["es"]) == [0, 4, 16, 12, 13, 18]


def test_decode_text():
    assert decode_text("L olnh hohskdqwv", alphabets["en"]) == [
        ("I like elephants", 3),
        ("E hega ahaldwjpo", 7),
        ("V yvxr ryrcunagf", 16),
        ("M pmoi ipitlerxw", 25),
        ("S vsuo ovozrkxdc", 19),
        ("X axzt tatewpcih", 14)
    ]
    assert decode_text("Oh jxvwdp ñrv hñhidpwhv", alphabets["es"]) == [
        ("Me gustan los elefantes", 3),
        ("Ia cqopwj hlo ahabwjpao", 7),
        ("Wo qfdelx vzd ovoplxeod", 19),
        ("As ujhiob zdh szstobish", 15),
        ("Zr tighña ycg ryrsñahrg", 16),
        ("Un odbcjv txb ntnñjvcnb", 21),
    ]


if __name__ == "__main__":
    test_count_letters()
    
    test_cesar_cipher()
    test_code_text()
    
    test_remove_special_characters()
    
    test_cesar_decode()
    test_decode_text()
