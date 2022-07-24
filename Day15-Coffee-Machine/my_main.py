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


def compare_resources(k_ingred, k_resources):
            """Check either the resources required are available or not"""
            for (k1,v1) , (k2,v2) in zip(k_ingred.items(),k_resources.items()):
                if v1 > v2:
                    print(f"Sorry there is not enough {k1}.")


def coin_process(p,n,d,q):
    """Sum the total amount of money in dollars"""
    p = 0.01 * p
    n = 0.05 * n
    d = 0.10 * d
    q = 0.25 * q
    total = p + n + d + q
    return total


def cost_compare(payment, cost):
    """Check if money amount is greater than cost of coffee"""
    if payment < cost:
        print(f"Sorry that's not enough money. Coffee cost ${cost} Money refunded.")
    else:
        if payment > cost:
            return_amount = payment - cost
        else:
            global profit
            profit += cost
            return profit

profit = 0
is_on = True
while is_on:
    command = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if command == "off":
        print("Shutting down")
        is_on = False
    elif command == "report":
        for key, value in resources.items():
            print(f"{key} : {value}")
        print(f"Money : ${profit}")

    elif command in ["espresso", "latte", "cappuccino"]:
        coffee = MENU[command]
        print(coffee)

        # def ingredients(ingred):
        #     water = ingred["water"]
        #     milk = ingred["milk"]
        #     coffee = ingred["coffee"]
        #     print(water, coffee, milk)
        # 
        # ingredients(ingred = coffee_name["ingredients"])

        # print(command)
        # for k,v in coffee_name.items():
        #     print(f"{k}:{v}")

        compare_resources(coffee["ingredients"], resources)
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        user_payment = coin_process(p = pennies, n = nickles, d = dimes, q = quarters)
        print(user_payment)
        print(profit)

        cost_compare(payment =  user_payment, cost = coffee["cost"])



    else:
        print("Invalid input")