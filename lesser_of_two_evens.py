def lesser_of_two_evens(a,b):
    '''Check the lesser of two given numbers if they're even,
    but returns the greater if one or both numbers are odd'''
    
    if a % 2  == 0 and b % 2 == 0:
        if a < b:
            return a
        return b

    elif a % 2 == 1 or b % 2 == 1:
        if a < b:
            return b
        return a

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))