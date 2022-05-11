def makes_twenty(n1,n2):
    '''Code returns True if the sum of the integers is 20 or one of the integers is 20,
    False if any of the conditions isn't met
    '''

    #create an empty list
    numbers = []
    
    numbers.append(n1)
    numbers.append(n2)

    if 20 in numbers:
        return True
        
    elif sum(numbers) == 20:
        return True
    
    return False
   

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))