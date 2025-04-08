from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
    options = menu.get_items()
    client_order = input(f"Which coffee would you like to order?({options})")
    if client_order == "off":
        is_on = False
    elif client_order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(client_order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        