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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def get_report():
    print(f"Water: {resources['water']}.ml")
    print(f"Milk: {resources['milk']}.ml")
    print(f"Coffee: {resources['coffee']}.g")
    print(f"Money: {profit}")


def is_resources_sufficient(ordered_ingredients, order):
    """Returns True when order can be made, otherwise returns False."""
    for item in ordered_ingredients:
        if ordered_ingredients[item] >= resources[item]:
            print(f"Sorry there's not enough {item} for {order}!")
            return False
        return True

def process_coins():
    """Returns the total calculated from the coins inserted"""
    print("Please insert coins: ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money, cost):
    """Returns True when the payment is accepted, or False if money is insufficient"""
    if money >= cost:
        change = round(money - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry there's not enough money!")
        return False


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        get_report()
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"], choice):
            payment = process_coins()
            is_transaction_successful(payment, drink["cost"])

