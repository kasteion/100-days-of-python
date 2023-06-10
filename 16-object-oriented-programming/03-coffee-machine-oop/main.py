from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
menu.menu = [
    MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
    MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
    MenuItem(name="cappuccino", water=250, milk=100, coffee=24, cost=3.0),
]

coffee_maker = CoffeeMaker()
coffee_maker.resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_machine = MoneyMachine()


def coffee():
    machine_on = True
    while machine_on:
        option = input(f"What would you like? ({menu.get_items()}): ").lower()

        if option == "off":
            machine_on = False
        elif option == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            if option in menu.get_items().split("/"):
                drink = menu.find_drink(option)
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)

            else:
                print("Sorry we don't have that drink.")


coffee()
