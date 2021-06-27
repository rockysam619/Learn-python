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


def sufficient_resource(ingredients):
    """return True is resources are enough for order"""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Return the total calculated from coins"""
    print("Please insert coins.")
    total = int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: "))*0.10
    total += int(input("how many nickels?: "))*0.05
    total += int(input("how many pennies?: "))*0.01
    return total

def enough_money(money_received, drink_cost):
    """Return true if payment is accepted """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your cange of ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")


def make_coffee(drink_name, ingredients):
    """Deduct the required ingredients from resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name} ☕")


#TODO 1 : Ask “What would you like? (espresso/latte/cappuccino):”
is_on = True
while is_on:
    order = input("\nWhat would you like? (espresso/latte/cappuccino):")
    if order == "off":
        is_on = False
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[order]
        if sufficient_resource(drink['ingredients']):
            payment = process_coins()
            if enough_money(payment, drink['cost']):
                make_coffee(order, drink['ingredients'])






