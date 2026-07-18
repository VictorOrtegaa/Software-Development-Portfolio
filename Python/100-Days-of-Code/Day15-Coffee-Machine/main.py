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

profit = 0

#PRINT report
# check resources
# process coins
#check transactino succesful
# make coffee




def RESOURCES(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def coins ():
    print("Insert coins ")
    total = int(input("How many quarters? :")) * 0.25
    total += int(input("How many dimes? :")) * 0.10
    total += int(input("How many nickles? :")) * 0.05
    total += int(input("How many pennies? :")) * 0.01
    return total

def transaction (money_given, drink_price):
    if money_given >= drink_price:
        change = round(money_given - drink_price,2)
        print(f"Here's your change ${change}")
        global profit
        profit += drink_price
        return True
    else:
        print(f"Sorry there is not enough ${money_given}. Money refunded ")
        return False



def coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Have a nice day !")


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if RESOURCES(drink["ingredients"]):
            payment = coins()
            if transaction(payment, drink["cost"]):
                coffee(choice, drink["ingredients"])




