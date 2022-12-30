from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

call_menu = Menu()
make_order = CoffeeMaker()
cash = MoneyMachine()
off = False


while off != True:
    ask_order = input(f"What would you like? ({call_menu.get_items()}):")
    if ask_order == 'report':
        make_order.report()
        cash.report()
    elif ask_order == 'off':
        off = True
    else:
        find_order = call_menu.find_drink(ask_order) 
        ask_money = cash.make_payment(find_order.cost)
        check_order = make_order.is_resource_sufficient(find_order)
        if check_order == True and ask_money == True:
            make_drink = make_order.make_coffee(find_order) 
        
    
    
