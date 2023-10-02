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

    # TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
    # TODO: 2. Turn off the coffe machine by entering "off" to the prompt
    # TODO: 3. Print report


def print_report(money):
    print(f"Water: {resources['water']} ml ")
    print(f"Milk: {resources['milk']} ml ")
    print(f"Coffee: {resources['coffee']} ml ")
    print(f"Money: ${money}")


def check_resources(water, coffee, milk, machine_resources):
    if water > machine_resources['water']:
        print("Sorry there is not enough water.")
    elif coffee > machine_resources['coffee']:
        print("Sorry there is not enough coffee.")
    elif milk > machine_resources['milk']:
        print("Sorry there is not enough milk.")
    else:
        return True


def insert_coins(drink_cost):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    coins_inserted = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    print(coins_inserted)
    return coins_inserted


def make_drink(water, coffee, milk):
    global resources
    resources['milk'] -= milk
    resources['water'] -= water
    resources['coffee'] -= coffee



def coffee_machine():
    select = ''
    current_money = 0
    while select != 'off':
        select = input("What would you like? (espresso/latte/cappuccino): ")
        if select == 'report':
            print_report(current_money)
        elif select == 'espresso':
            water_needed = MENU['espresso']['ingredients']['water']
            coffe_needed = MENU['espresso']['ingredients']['coffee']
            milk_needed = 0
            cost = MENU['espresso']['cost']
        elif select == 'latte':
            water_needed = MENU['latte']['ingredients']['water']
            coffe_needed = MENU['latte']['ingredients']['coffee']
            milk_needed = MENU['latte']['ingredients']['milk']
            cost = MENU['latte']['cost']
        elif select == 'cappuccino':
            water_needed = MENU['cappuccino']['ingredients']['water']
            coffe_needed = MENU['cappuccino']['ingredients']['coffee']
            milk_needed = MENU['cappuccino']['ingredients']['milk']
            cost = MENU['cappuccino']['cost']
        else:
            print("Wrong choice.")

        if select == 'latte' or select == 'cappuccino' or select == 'espresso':
            check = check_resources(water_needed, coffe_needed, milk_needed, resources)
            if check:
                money_given = insert_coins(cost)
                if money_given < cost:
                    print("Sorry that's not enough money. Money refunded. ")
                elif money_given > cost:
                    make_drink(water_needed, coffe_needed, milk_needed)
                    current_money += cost
                    print(f"Here is {round(money_given - cost,2)} in change.")
                    print(f"Here is your {select} . Enjoy!")
                else:
                    make_drink(water_needed, coffe_needed, milk_needed)
                    current_money += cost
                    print(f"Here is your {select} . Enjoy!")

    return


coffee_machine()