
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
profit=0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return  True
def process_coin():
    print("Please Insert a coin ! ")
    total = int(input("How many quarters? (२५ पैसा)?: ")) * 25
    total += int(input("How many dimes?(१० पैसा)?: ")) * 10
    total += int(input("how many nickles?(५ पैसा)?: ")) * 5
    total += int(input("how many pennies?(१ पैसा)?: ")) * 1
    return total
def check_transaction(money_received,  drink_cost,   ):

    if money_received >=drink_cost:
        change=round(money_received - drink_cost)
        print("\n")
        print(f"Here is Your  RS {change} ")
        global  profit
        profit+=drink_cost
        return True
    else :
        print("Sorry that's not enough monrey ")
        for drink in MENU:
            price = MENU[drink]["cost"]
            print(f"{drink.title()} - Rs. {price}")


def make_coffe(drink_name , order_ingredients ):
    for item in order_ingredients:

        order_ingredients[item]-=resources[item]
    print(f"Enjoy your drink {drink_name}")


is_on= True
while is_on:
    choice=input("What would you like? espresso ☕ /latte🧋/cappuccino 🥐☕:")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs {profit}")
    else :
        drink=MENU[choice]
        if resources_sufficient(drink["ingredients"]):
            payment=process_coin()
            if check_transaction(payment,drink["cost"]):
                make_coffe(choice, drink["ingredients"])