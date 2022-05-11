def convert_num_string(num):
    '''Converts an integer to string
    '''
    numbers = ['one', 'two', 'three', 'four',
'five']
    if num not in range(1,6):
        return 'invalid input...Or not in range'
    return numbers[num - 1]

num = int(input('Enter a number between 1-5 inclusive\n>>> '))
result_1 = convert_num_string(num)
print(result_1)



def convert_string_num(num_1):
    '''Converts a string to integer
    '''
    numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    numbers_1 = ['one', 'two', 'three', 'four', 'five']
    if num_1.lower() not in numbers_1:
        return 'invalid input...Or not in range'
    return numbers[num_1.lower()]

num_1 = input('Enter your figure btw 1-5 in words\n>>> ')
result_2 = convert_string_num(num_1)
print(result_2)
