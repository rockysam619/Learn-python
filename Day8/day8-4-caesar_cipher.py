#Caesar Cipher function 
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

keepon = True
while keepon:
    
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%26

    def caesar(start_text, shift_amount, direction):
        end_text = ""
        if direction == "decode":
                shift_amount*=-1

        for letter in start_text:
            if letter in alphabet:
                x = alphabet.index(letter)
                if x + shift_amount > 25:
                    letter = alphabet[x + shift_amount - 26] # Taking care of index out of range error
                else:
                    letter = alphabet[x + shift_amount]

                end_text += letter
            else:
                end_text += letter

        print(f"{direction}d text is {end_text}")
    
    caesar(text, shift, direction)
    answer = input("Would you like to continue using the program? Yes or No?: ").lower()
    if answer == "no":
        keepon = False
        print("\nGoodbye")




