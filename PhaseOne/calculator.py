def calculator(a,b,operation='add'):
    results = a + b
    return results

a = int(input("Enter first number "))
b = int(input("Enter second number "))
print(calculator(a,b))

#Will come back to this when I learn more about boolen and if/else to build true calculator

'''
Completed boots.dev Cafe Order Summary with code 

def build_order_summary(drink_name, quantity, price_each, is_iced):
    total = quantity * price_each
    if is_iced == True:
        is_iced = "(iced)"
    elif is_iced == False:
        is_iced = "(hot)"
    return (f"Drink: {drink_name}\nQuantity: {quantity}\nTotal: {total} coins {is_iced}")

'''