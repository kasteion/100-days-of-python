# Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_pass = ""
for l in range(0, nr_letters):
    easy_pass += random.choice(letters)

for s in range(0, nr_symbols):
    easy_pass += random.choice(symbols)

for n in range(0, nr_numbers):
    easy_pass += random.choice(numbers)

print("Easy Version:")
print(easy_pass)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

characters = []
for l in range(0, nr_letters):
    characters.append(random.choice(letters))

for s in range(0, nr_symbols):
    characters.append(random.choice(symbols))

for n in range(0, nr_numbers):
    characters.append(random.choice(numbers))

random.shuffle(characters)

print("\nHard Version:")
print(''.join(characters))
