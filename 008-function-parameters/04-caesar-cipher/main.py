from art import logo
from os import name, system

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def caesar(input_text, shift_amount, direction):
    output_text = ""
    for letter in input_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if direction == 'encode':
                index += shift_amount
            else:
                index -= shift_amount
            output_text += alphabet[index]
        else:
            output_text += letter
    print(f"Here's the {direction}d result: {output_text}")


again = 'yes'
while again == 'yes':
    clear()
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(text, shift, direction)

    again = input("Type 'yes' if you want to go again, Otherwise type 'no' ").lower()

print("Goodbye")