from art import logo
import random

# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

number_to_guess = random.randint(1, 100)
guess = 0
print(logo)
print("Welcome to the Number Guessing Game!")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "hard":
    guesses = 5
else:
    guesses = 10

while guesses > 0 and guess != number_to_guess:
    print(f"You have {guesses} attempts remaining to guess the number.")
    guesses -= 1
    guess = int(input("Make a guess: "))
    if guess > number_to_guess:
        print("Too high.")
    elif guess < number_to_guess:
        print("To low.")

    if guesses > 0:
        print("Guess again.")

if guess == number_to_guess:
    print(f"You got it! The answer was {guess}.")
elif guesses == 0:
    print("You've run out of guesses, you lose.")
