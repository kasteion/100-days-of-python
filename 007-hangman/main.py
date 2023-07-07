import random
from hangman_art import logo, stages
from hangman_words import word_list
from os import system, name


def clear():
    # For windows
    if name == "nt":
        _ = system("cls")
    # For mac / linux
    else:
        _ = system("clear")


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
display = ["_"] * word_length

print(logo)

while not end_of_game:

    guess = input("Guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for idletter, letter in enumerate(chosen_word):
        if letter == guess:
            display[idletter] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a live.")
        lives -= 1

    if lives == 0:
        end_of_game = True
        print("You lose")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
