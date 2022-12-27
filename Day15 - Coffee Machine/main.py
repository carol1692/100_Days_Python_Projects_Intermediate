#!/usr/bin/env python3


import menu

################################

def print_report():
    for item in menu.resources:
        if item == 'water' or item == 'milk':
            print(f'{item.title()}: {menu.resources[item]}ml')
        elif item == 'coffee':
            print(f'{item.title()}: {menu.resources[item]}g')
        else:
            print(f'{item.title()}: ${menu.resources[item]}')

def check_resources(drink_option):
    enough_ingredients = True
    for ingredient in menu.MENU[drink_option]['ingredients']:
        dict_recipe = menu.MENU[drink_option]['ingredients']
        if menu.resources[ingredient] < dict_recipe[ingredient] :
            print(f'Sorry there is not enough {ingredient}')
            enough_ingredients = False
    return enough_ingredients

def order(drink, resources_enough):
        recipe = menu.MENU[drink]['ingredients']
        
        if resources_enough == True:
            print(f'Starting to prepare {user_input} ☕')
            for ingredient in recipe:
                reservatorio = menu.resources[ingredient] - menu.MENU[drink]['ingredients'][ingredient]
                menu.resources[ingredient] = reservatorio
        

def check_coins(drink):
    print('Please insert coins.')
    #quarter = 0.25, dimes = 0.1 ,nickles = 0.05, pennies = 0.01
    count_total = 0
    drink_price = menu.MENU[drink]['cost']
    print(f"preço da bebida:{drink_price}")
    count_total = int(input('How many quarters?: ') )*0.25
    count_total += int(input('How many dimes?: ') )*0.1
    count_total += int(input('How many nickles?: ') )*0.05
    count_total += int(input('How many pennies?: ') )*0.01
    if count_total >= drink_price:
        change = count_total - drink_price
        print(f'Here is ${change:.2f} in change')
        menu.resources['money'] = count_total - change
    else:
        print(f"Sorry that's not enough money. Money refunded")
    
    print(count_total)
    print(menu.resources['money'])
    return  count_total
    
    
    
    

            
################################
off = False
count = 0
while off == False:
    user_input = input('What would you like? (espresso/latte/cappuccino): ')
    if user_input == 'report':
        print_report()
    elif user_input == 'off':
        off = True
    else:
        money_inserted = check_coins(user_input)
        resources_sufficient = check_resources(user_input) 
        order(user_input, resources_sufficient)
    

    

