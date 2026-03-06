from menu_day_15 import MENU, resources
from os import system
money=0
available=True
system("cls")

def check_status():
    if coffee!="espresso":
        if MENU[coffee]["ingredients"]["water"]>resources["water"]:
            print("Not enough water!")
            return False
        elif MENU[coffee]["ingredients"]["milk"]>resources["milk"]:
            print("Not enough milk!")
            return False
        elif MENU[coffee]["ingredients"]["coffee"]>resources["coffee"]:
            print("Not enough coffee!")
            return False
    elif coffee=="espresso":
        if MENU[coffee]["ingredients"]["water"]>resources["water"]:
            print("Not enough water!")
            return False
        elif MENU[coffee]["ingredients"]["coffee"]>resources["coffee"]:
            print("Not enough coffee!")
            return False
    return True

def update_machine():
    global money
    input_money=0
    print("Please insert coins")
    q=int(input("How many quaters? "))
    d=int(input("How many dimes? "))
    n=int(input("How many nickels? "))
    p=int(input("How many pennies? "))
    input_money= 0.25*q+0.1*d+0.05*n+0.01*p;

    if input_money>=MENU[coffee]["cost"]:
        return_money=input_money-MENU[coffee]["cost"]
        money+=MENU[coffee]["cost"]
        print(f"Here is ${return_money:0.2f} in change")

        resources["water"]-=MENU[coffee]["ingredients"]["water"]
        resources["coffee"]-=MENU[coffee]["ingredients"]["coffee"]

        if coffee!="espresso":
            resources["milk"]-=MENU[coffee]["ingredients"]["milk"]
        else:
             resources["milk"]


        if coffee=="espresso":
            print("Here is your espresso ☕️. Enjoy!")
        elif coffee=="latte":
            print("Here is your latte ☕️. Enjoy!")
        else:
            print("Here is your cappuccino ☕️. Enjoy!")
        
    else:
        print("Sorry that's not enough money. Money refunded. ")
        
while(available):
    coffee = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if coffee=="report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney ${money}  ")
    elif coffee in MENU:
        if check_status():
            update_machine()
    elif coffee=="off":
        available=False
    else:
        print("INVALID INPUT!")