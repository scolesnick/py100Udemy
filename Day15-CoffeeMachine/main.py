# Make coffee machine that provides 3 recipes
# Coffee machine is coin operated

import data

resources = data.resources
MENU = data.MENU
running = True
resources['money'] = 0.0
notEnough = []


def updateResources(water, milk, coffee):
    resources['water'] = water
    resources['milk'] = milk
    resources['coffee'] = coffee


def updateCash(money):
    resources['money'] += money

def getDifference(recipe):
    try:
        recipeWater = MENU[recipe]['ingredients']['water']
    except:
        recipeWater = 0
    try:
        recipeMilk = MENU[recipe]['ingredients']['milk']
    except:
        recipeMilk = 0
    try:
        recipeCoffee = MENU[recipe]['ingredients']['coffee']
    except:
        recipeCoffee = 0
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    return water - recipeWater, milk - recipeMilk, coffee - recipeCoffee


def resourceAvailable(recipe):
    w, m, c = getDifference(recipe)

    enoughWater = w >= 0
    enoughMilk = m >= 0
    enoughCoffee = c >= 0
    if enoughMilk and enoughWater and enoughCoffee:
        return True

    notEnough.clear()
    if not enoughCoffee:
        notEnough.append('Coffee')
    if not enoughMilk:
        notEnough.append('Milk')
    if not enoughWater:
        notEnough.append('Water')
    return False


def getResource():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def getMoney():
    coins = ['Quarter(s)','Dime(s)','Nickel(s)','Pennie(s)']
    for c in coins:
        intVal = False
        while not intVal:
            try:
                idx = coins.index(c)
                c = int(input(f"How many {c}?: "))
                coins[idx] = c
                intVal = True
            except:
                print("Please enter a number")
    # Return total value
    total = (coins[0]*25 + coins[1]*10 + coins[2]*5 + coins[3])/100
    return total


def processMoney(amount, response):
    cost = MENU[response]['cost']
    costDifference = amount - cost
    if costDifference == 0.0:
        updateCash(money=cost)
        return True
    elif costDifference > 0.0:
        updateCash(money=cost)
        print(f"Here is ${costDifference:.2f} in change.")
        return True
    return False


while running:
    options = ['espresso', 'latte', 'cappuccino', 'report', 'off']
    response = ''
    while response.lower() not in options:
        response = input("What would you like? (espresso/latte/cappuccino): ")
    if response == 'report':
        getResource()
    elif response == 'off':
        print("Shutting off")
        running = False
    elif resourceAvailable(response):
        mon = getMoney()
        if processMoney(mon, response):
            print(f"Here is your {response} Enjoy!")
            w, m, c = getDifference(response)
            updateResources(water=w,milk=m,coffee=c)
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Sorry there is not enough {', '.join(notEnough)}.")
