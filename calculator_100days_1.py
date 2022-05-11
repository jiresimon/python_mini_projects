def add(n1, n2):
    '''all four user defined functions allow the addition of only two numbers
    '''
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

#using the knowledge of a dictionary with keys and values to access our functions
    operations = {'+': add, 
'-': subtract, 
'*': multiply,
'/': divide
}
    for symbols in operations:
    #this will loop through the dictionary and show the user the various operations embedded in the calculator
        print(symbols)
    
    operation_symbol = input('pick an operation from the symbols above: ')

    n2 = float(input('What\'s the second number: '))

    if operation_symbol == '+':
        result = operations[operation_symbol]
        #call the function
        final_answer = result(n1,n2)
        #next code allows you to see the output because we're using the keyword 'return and not 'print' in our user defined function above
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

