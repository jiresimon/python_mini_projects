def animal_crackers(text):
    '''Takes a two word string and returns
    True if both words begin with the same letter'''


    #text = text.lower()
    text_1 = text.split()

    word_1 = text_1[0]
    word_2 = text_1[1]
    
    if word_1[0] == word_2[0]:
        return True
    return False

print(animal_crackers('Levelheaded llama'))
print(animal_crackers('Crazy Kangaroo'))