from art import logo
from os import name, system


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


print(logo)
print("Welcome to the secret auction program.")

bids = []

end_auction = False

while not end_auction:

    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    bids.append({"name": name, "bid": bid})

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ").lower()

    clear()

    if other_bidders == "no":
        end_auction = True

winner = {"name": "", "bid": 0}

for bid in bids:
    if bid["bid"] > winner["bid"]:
        winner["name"] = bid["name"]
        winner["bid"] = bid["bid"]

print(f"The winner is {winner['name']} with a bid of ${winner['bid']}")

