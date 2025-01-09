# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encode(original_text, shift_amount):
    encr_list = []
    for letter in original_text:
        if letter not in alphabet:
            encr_list.append(letter)
        elif alphabet.index(letter) + shift_amount < 26:
            letter = alphabet[alphabet.index(letter) + shift_amount]
            encr_list.append(letter)
        elif alphabet.index(letter) + shift_amount >= 26:
            letter = alphabet[alphabet.index(letter) - 26 + shift_amount]
            encr_list.append(letter)
    result1 = "".join(encr_list)
    print(result1)

def decode(original_text, shift_amount):
    decode_list = []
    for char in original_text:
        if char in alphabet:
            char = alphabet[alphabet.index(char) - shift_amount]
            decode_list.append(char)
        else:
            decode_list.append(char)
    result2 = "".join(decode_list)
    print(result2)

start = True
while start == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encode(text, shift)
    else:
        decode(text, shift)

    user_choice = input("Do you want to start again? \nType 'yes' or 'no' ")
    if user_choice == "no":
        start = False












