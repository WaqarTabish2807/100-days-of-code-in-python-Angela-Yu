from glob import glob
from data import MENU
from art import logo
print (logo)
is_on = True
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry, there is not enough {item}.")
            return False 
    return True

def process_coins():
    print("Please insert coins.")
    total= float(input("How many quarters?: ")) * 0.25
    total+= float(input("How many dimes?: ")) * 0.1
    total+= float(input("How many nickles?: ")) * 0.05
    total+= float(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print("")
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else: 
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕. Enjoy!")

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino)").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice,drink["ingredients"])




    