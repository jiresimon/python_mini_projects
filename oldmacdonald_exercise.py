def old_macdonald(name):
    '''Capitalizes the first and fourth letters of a name'''

    #capitalize the first letter
    name = name.capitalize()
    name_1 = name[:3]
    
    #Get the fourth letter using it's index
    name_2 = name[3]

    #capitalize the fourth letter
    name_2 = name_2.capitalize()
    
    name_3 = name[4:]
    return name_1 + name_2 + name_3

print(old_macdonald('macdonald'))
