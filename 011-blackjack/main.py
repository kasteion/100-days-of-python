# Blackjack Project

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# Our Blackjack House Rules

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The  Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

###############################################################
import random
from art import logo
from os import name, system

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def get_score(cards):
    total = 0
    for card in cards:
        total += card
    return total


def replace_aces(cards):
    for i in range(0, len(cards)):
        if cards[i] == 11:
            cards[i] = 1
    return cards


def deal(cards):
    score = get_score(cards)
    card = random.choice(deck)
    cards.append(card)
    if score + card > 21 and 11 in cards:
        cards = replace_aces(cards)
    score = get_score(cards)
    return {"cards": cards, "score": score}


def print_player_game(player_game):
    print(
        f"\tYour cards: {player_game['cards']}, current score: {player_game['score']}"
    )


def print_computer_game(computer_game, secret):
    if secret:
        print(f"\tComputer's first card: {computer_game['cards'][0]}")
    else:
        print(
            f"\tComputer's cards: {computer_game['cards']}, current score: {computer_game['score']}"
        )


def keep_playing(player_game, computer_game):
    if player_game["score"] < 21:
        print_computer_game(computer_game, True)
        answer = input(
            "Type 'y' to get another card, type 'n' to pass: ").lower()
        if answer == "y":
            return True
        else:
            return False
    else:
        return False


def get_winner(player_game, computer_game):
    player_score = player_game['score']
    computer_score = computer_game['score']
    print(f"\tYour final hand: {player_game['cards']}, final score: {player_score}")
    print(f"\tComputer's final hand: {computer_game['cards']}, final score: {computer_score}")

    if player_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif computer_score > player_score:
        if computer_score == 21:
            return "Lose, opponent has Blackjack 😱"
        return "You lose 😤"
    elif player_score > computer_score:
        return "You win 😃"
    else:
        return "Draw 🙃"


def blackjack():
    clear()
    print(logo)

    player_game = deal([])
    computer_game = deal([])
    player_game = deal(player_game["cards"])
    computer_game = deal(computer_game["cards"])
    print_player_game(player_game)

    hit = keep_playing(player_game, computer_game)

    while hit and player_game["score"] < 21:
        player_game = deal(player_game["cards"])
        print_player_game(player_game)
        hit = keep_playing(player_game, computer_game)

    while computer_game["score"] < 17:
        computer_game = deal(computer_game["cards"])

    print(get_winner(player_game, computer_game))

    if input(
            "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
        blackjack()


play = input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if play == "y":
    blackjack()
