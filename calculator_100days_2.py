def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


continue_arithmetic = True

while continue_arithmetic:
    
    n1 = float(input('What\'s the first number: '))

    operations = ('+', '-', '*', '/')

    for symbols in operations:
    #this will loop through the tuple and show the user the various operations embedded in the calculator
        print(symbols)
    
    operation_symbol = input('pick an operation from the symbols above: ')

    n2 = float(input('What\'s the second number: '))

    if operation_symbol == '+':
        print(f' {n1} {operation_symbol} {n2} = {add(n1, n2)}')

    elif operation_symbol == '-':
        print(f' {n1} {operation_symbol} {n2} = {subtract(n1, n2)}')

    elif operation_symbol == '/':
        print(f' {n1} {operation_symbol} {n2} = {divide(n1, n2)}')

    elif operation_symbol == '*':
        print(f' {n1} {operation_symbol} {n2} = {multiply(n1, n2)}')
    
    user_input = input('Press "y" to continue or "n" to stop:\n>>> ' )
    if user_input.lower() == 'n':
        continue_arithmetic = False
        print('Have a lovely day')








