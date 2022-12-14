from data import resources
from data import MENU

profit = 0

is_on = True

def is_ingredients_enough(is_ingredients_enough):

    for item in is_ingredients_enough:
        if  is_ingredients_enough[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False

def Process_coin():
    print("Insert coin")

    total = int(input("How many quarters?"))*0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total

def is_transaction_successful(money_received,drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)

        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_name,is_ingredients_enough):
    for item in is_ingredients_enough:
        resources[item] -= is_ingredients_enough[item]
    print(f"Here is your {drink_name}")





while is_on:
    choice = input("What would like to drink (espresso/latte/cappuccino)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water:{resources['water']}")
        print(f"Milk:{resources['milk']}")
        print(f"Coffee:{resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_ingredients_enough (drink["ingredients"]):
           payment = Process_coin()
           if is_transaction_successful(payment,drink["cost"]):
              make_coffe()


