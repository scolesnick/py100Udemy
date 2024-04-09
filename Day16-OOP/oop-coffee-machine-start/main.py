# Repeat Coffee Machine project using OOP and the classes defined
# 1. Print report
# 2. Check resources sufficient?
# 3. Process coins.
# 4. Check transaction successful?
# 5. Make Coffee.

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

running = True
cm.report()
options = ['espresso', 'latte', 'cappuccino', 'report', 'off']

while running:
    response = ''
    while response.lower() not in options:
        response = input("What would you like? (espresso/latte/cappuccino): ")
    if response == 'report':
        cm.report()
        money.report()
    elif response == 'off':
        print("Shutting off")
        running = False
    else:
        item = menu.find_drink(response)
        if item is not None:
            if cm.is_resource_sufficient(item):
                if money.make_payment(item.cost):
                    cm.make_coffee(item)
