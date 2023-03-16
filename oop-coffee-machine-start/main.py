from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

active = True
jarvis = CoffeeMaker()
watson = MoneyMachine()
menu = Menu()

while active:
    user_input = input(f"Choose from the following items : {menu.get_items()} \n").lower()
    if user_input == 'off':
        active = False
    elif user_input == 'report':
        jarvis.report()
        watson.report()
    elif menu.find_drink(user_input) is not None:
        drink = menu.find_drink(user_input)
        if jarvis.is_resource_sufficient(drink):
            if watson.make_payment(drink.cost):
                jarvis.make_coffee(drink)

        else:
            print(f'There is not enough resources to make the {drink.name}')
