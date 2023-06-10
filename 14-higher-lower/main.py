from random import choice
from art import logo, vs
from game_data import data
from os import name, system


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def pick_ig_account(not_this_account):
    """ Picks a random account that is not the same as the not_this_account"""
    ig_account = choice(data)
    if ig_account == not_this_account:
        ig_account = pick_ig_account()
    return ig_account


def check_answer(account_a, account_b, answer):
    """ Check the answer and return True if the anwer is correct and False if not"""
    if answer == "a" and account_a["follower_count"] >= account_b["follower_count"]:
        return True
    elif answer == "b" and account_a["follower_count"] <= account_b["follower_count"]:
        return True
    else:
        return False


def game():
    """ This is the game function """
    game_end = False
    score = 0
    account_a = pick_ig_account({'name': ""})

    while not game_end:
        clear()

        account_b = pick_ig_account(account_a)

        print(logo)

        if score > 0:
            print(f"You're right! Current score: {score}")

        print(
            f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}."
        )

        print(vs)
        print(
            f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}."
        )

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if check_answer(account_a, account_b, answer):
            score += 1
            account_a = account_b
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_end = True


game()
