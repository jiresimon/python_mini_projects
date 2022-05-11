def master_yoda(text):
    '''Function reverses a given statement'''

    text = text.split()

    #use the reverse method to reverse the elements in the list
    text_1 = text.reverse()

    #join the reversed list 
    text_1 = ' '.join(text)
    return text_1

print(master_yoda('i am home'))
print(master_yoda('we are ready'))