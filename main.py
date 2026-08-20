#list of alphabet and morse code characters are stored in data file
from data import mcode_list, letters_list, my_logo


#function for transforming string to morse code
def txt_to_morse(txt):
    tmp_str = ""
    my_word = txt
    for i in my_word:
        if i in letters_list:
            tmp_str += mcode_list[letters_list.index(i)] + " "
    print(f"Morse code for entered text is: {tmp_str}")

#function for transforming morse code to text
def morse_to_txt(morse_code):
    tmp_str = ""
    code_list = morse_code.split()
    for i in code_list:
        if i in mcode_list:
            tmp_str += letters_list[mcode_list.index(i)]
    print(f"Text of entered morse code is: {tmp_str}")


start = False
print(my_logo)
while start == False:
    print("\n")
    func_input = input("Based on selected number input will be transformed in following manner:"
                       "\n1 - For transforming text to morse code"
                       "\n2 - For transforming morse code to text"
                       "\n3 - For Exiting"
                       "\nEnter your choice: ")
    if func_input == "1":
        my_input = input("Enter a word or combination of number and letters from English alphabet: ").upper()
        txt_to_morse(my_input)
    elif func_input == "2":
        my_input = input("Enter a morse code you want to transform to text: ")
        morse_to_txt(my_input)
    elif func_input == "3":
        start = True
    else:
        print("Invalid input")
