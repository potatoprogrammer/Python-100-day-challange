from library import MENU, resources

turn_off = False
money = 0

def coins(price, product):
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    user_quarters = int(input("how many quarters: "))
    user_quarters *= quarters
    user_dimes = int(input("how many dimes: "))
    user_dimes *= dimes
    user_nickles = int(input("how many nickles: "))
    user_nickles *= nickles
    user_pennies = int(input("how many pennies: "))
    user_pennies *= pennies

    user_total =  user_quarters + user_dimes + user_nickles + user_pennies

    if user_total >= price:
        print(f"Here is ${user_total - price} in change.")
        print(f"Here is your {product} ☕️Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


while not turn_off:
    client_request = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if client_request == "espresso":
        print(f"Total: ${MENU['espresso']['cost']}")
        print("Please insert coins.")
        if coins(MENU['espresso']['cost'], "espresso"):
            if resources['water'] >= MENU['espresso']['ingredients']['water'] and \
                    resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
                money += MENU['espresso']['cost']
                resources['water'] -= MENU['espresso']['ingredients']['water']
                resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
            else:
                print("There is not enough ingredients for this item, sorry.")
    elif client_request == "latte":
        if resources['water'] >= MENU['latte']['ingredients']['water'] and \
                resources['coffee'] >= MENU['latte']['ingredients']['coffee'] and \
                resources['milk'] >= MENU['latte']['ingredients']['milk']:
            print(f"Total: ${MENU['latte']['cost']}")
            print("Please insert coins.")
            if coins(MENU['latte']['cost'], "latte"):
                money += MENU['latte']['cost']
                resources['water'] -= MENU['latte']['ingredients']['water']
                resources['coffee'] -= MENU['latte']['ingredients']['coffee']
                resources['milk'] -= MENU['latte']['ingredients']['milk']
        else:
            print("There is not enough ingredients for this item, sorry.")
    elif client_request == "cappuccino":
        if resources['water'] >= MENU['cappuccino']['ingredients']['water'] and \
                resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee'] and \
                resources['milk'] >= MENU['cappuccino']['ingredients']['milk']:
            print(f"Total: ${MENU['cappuccino']['cost']}")
            print("Please insert coins.")
            if coins(MENU['cappuccino']['cost'], "cappuccino"):
                money += MENU['cappuccino']['cost']
                resources['water'] -= MENU['cappuccino']['ingredients']['water']
                resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
                resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
        else:
            print("There is not enough ingredients for this item, sorry.")
    elif client_request == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}")
        print(f"Money: ${money}")
    elif client_request == "off":
        print("The machine is turning down...")
        turn_off = True

