#creating user defined functions for arithmetic operations
#calculator allows only two variables for calculation

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#creating a dictionary that links our user input with the functions

# operations = {'+': add, 
# '-': subtract, 
# '*': multiply,
# '/': divide
# }

# n1 = int(input('What\'s the first number: '))


# for symbols in operations:
#this will loop through the dictionary and show the user the various operations embedded in the calculator
    # print(symbols)

# operation_symbol = input('pick an operation from the symbols above: ')

continue_arithmetic = True

while continue_arithmetic:
    
    n1 = int(input('What\'s the first number: '))

    operations = {'+': add, 
'-': subtract, 
'*': multiply,
'/': divide
}
    for symbols in operations:
    #this will loop through the dictionary and show the user the various operations embedded in the calculator
        print(symbols)
    
    operation_symbol = input('pick an operation from the symbols above: ')

    n2 = int(input('What\'s the second number: '))



    if operation_symbol == '+':
        result = operations[operation_symbol]
        final_answer = result(n1,n2)
        print(f' {n1} {operation_symbol} {n2} = {final_answer}')

    elif operation_symbol == '-':
        result = operations[operation_symbol]
        final_answer = result(n1,n2)
        print(f' {n1} {operation_symbol} {n2} = {final_answer}')

    elif operation_symbol == '/':
        result = operations[operation_symbol]
        final_answer = result(n1,n2)
        print(f' {n1} {operation_symbol} {n2} = {final_answer}')

    elif operation_symbol == '*':
        result = operations[operation_symbol]
        final_answer = result(n1,n2)
        print(f' {n1} {operation_symbol} {n2} = {final_answer}')
    
    user_input = input('Press "y" to continue or "n" to stop:\n>>>' )
    if user_input.lower() == 'n':
        continue_arithmetic = False
        print('Have a lovely day')








