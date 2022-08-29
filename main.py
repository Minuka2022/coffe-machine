from data import MENU
from data import resources
print("*********| Coffee prices |*********")
print("*** Espresso -- $2.5")
print("*** Latte -- $3.5")
print("*** cappuccino -- $4.5")
print("*********| pick your coffee |*********")


def user (user_choice):
    if user_choice == "espresso":
        return MENU["espresso"]

    elif user_choice == "latte":
        return MENU["latte"]

    elif user_choice == "cappuccino":
        return MENU["cappuccino"]


user_choice_coffee = user(user_choice = input("Enter your coffee type (espresso/latte/cappuccino)"))

def coin_cal (quarters,dimes,nickles,pennies):

    q = quarters * 0.25
    d = dimes * 0.10
    n = nickles * 0.05
    p = pennies * 0.01

    total = q+d+n+p
    return total


coin_cal(quarters=float(input("Enter quarters: ")))
coin_cal(dimes=float(input("Enter dimes: ")))
coin_cal(nickles=float(input("Enter nickles: ")))
coin_cal(pennies=float(input("Enter pennies")))

print(coin_cal())



 #if user == report the do below...

def resource_update (resources,user_choice_coffee):

    ingredients = user_choice_coffee["ingredients"]

    c_water = ingredients["water"]
    c_milk = ingredients["milk"]
    c_coffee = ingredients["coffee"]

    #resources

    r_water = resources["water"]
    r_milk = resources["milk"]
    r_coffee = resources["coffee"]


    #resource_update

    water = r_water - c_water
    milk = r_milk - c_milk
    coffee = r_coffee - c_coffee

    print(f"Water : {water}")
    print(f"milk : {milk}")
    print(f"coffee : {coffee}")


resource_update(resources,user_choice_coffee)





