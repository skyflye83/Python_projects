from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
choice = ""

while choice != "off":
    is_available = False
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "latte" or choice == "espresso" or choice == "cappuccino":
        drink = menu.find_drink(choice)
        is_available = coffee_maker.is_resource_sufficient(drink)
    else:
        print("Wrong choice")

    if is_available:
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
