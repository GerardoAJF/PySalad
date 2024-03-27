import alphabets as al

def select_alphabet():
    alphabet_options = tuple(al.alphabets.keys())
    
    print("Select the alphabet you want to use: ")
    print(f"The options are: {alphabet_options}")
    
    while True:
        alphabet_selected = input(">>")
        
        if alphabet_selected in alphabet_options:
            break
            
        print("Please enter a valid alphabet\n")
        
    return alphabet_selected
