es_alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

es_alphabet_values = tuple(zip(es_alphabet, range(1, len(es_alphabet) + 1)))

es_alphabet_num_to_letter = {num:letter for letter, num in es_alphabet_values}
es_alphabet_letter_to_num = {letter:num for letter, num in es_alphabet_values}

es_common_letters = ["e", "a", "o", "s", "r"]
