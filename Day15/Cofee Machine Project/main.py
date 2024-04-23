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


def is_resources_sufficient(ordered_ingredients):

    for item in ordered_ingredients:
        if ordered_ingredients[item] >= resources[item]:
            print("Sorry there's not enough water!")




is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        get_report()
    else:
        drink = MENU[choice]
        is_resources_sufficient(drink["ingredients"])

