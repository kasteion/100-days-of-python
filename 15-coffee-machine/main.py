LOGO = """
        /~~~~~~~~/|
       / /######/ / |
      / /______/ /  |
     ============ /||
     |__________|/ ||
      |\__,,__/    ||
      | __,,__     ||
      |_\====/%____||
      | /~~~~\ %  / |
     _|/      \%_/  |
    | |        | | /
    |__\______/__|/
    ~~~~~~~~~~~~~~


  ,----..                                                
 /   /   \            .--.,   .--.,                      
|   :     :  ,---.  ,--.'  \,--.'  \                     
.   |  ;. / '   ,'\ |  | /\/|  | /\/                     
.   ; /--` /   /   |:  : :  :  : :     ,---.     ,---.   
;   | ;   .   ; ,. ::  | |-,:  | |-,  /     \   /     \  
|   : |   '   | |: :|  : :/||  : :/| /    /  | /    /  | 
.   | '___'   | .; :|  |  .'|  |  .'.    ' / |.    ' / | 
'   ; : .'|   :    |'  : '  '  : '  '   ;   /|'   ;   /| 
'   | '/  :\   \  / |  | |  |  | |  '   |  / |'   |  / | 
|   :    /  `----'  |  : \  |  : \  |   :    ||   :    | 
 \   \ .'           |  |,'  |  |,'   \   \  /  \   \  /  
  `---`             `--'    `--'      `----'    `----'   
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

print(LOGO)


def print_report():
    for key in resources:
        unit = "ml"
        if key == "coffee":
            unit = "g"
        print(f"{key.capitalize()}: {resources[key]}{unit}")

    print(f"Money: ${money}")


def check_resources(drink):
    if drink in MENU:
        needed = MENU[drink]["ingredients"]
        for ingredient in needed:
            if resources[ingredient] < needed[ingredient]:
                print(f"Sorry there is not enough {ingredient}")
                return False
        return True
    else:
        print("Sorry we don't have that drink.")
        return False


def process_coins(quarters, dimes, nickels, pennies):
    return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01


def check_transaction(cost_amount, inserted_amount):
    global money
    if inserted_amount >= cost_amount:
        if inserted_amount > cost_amount:
            print(f"Here is ${round(inserted_amount - cost_amount, 2)} in change.")
        money += cost_amount
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(ingredients):
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]


def coffee():
    machine_on = True

    while machine_on:
        option = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if option == "off":
            machine_on = False
        elif option == "report":
            print_report()
        else:
            check = check_resources(option)
            if check:
                print("Please insert coins.")
                quarters = int(input("how many quarters?: "))
                dimes = int(input("how many dimes?: "))
                nickels = int(input("how many nickels?: "))
                pennies = int(input("how many pennies?: "))
                inserted_amount = process_coins(quarters, dimes, nickels, pennies)
                if check_transaction(MENU[option]["cost"], inserted_amount):
                    make_coffee(MENU[option]["ingredients"])
                    print(f"Here is your {option} ☕️. Enjoy!")


coffee()
