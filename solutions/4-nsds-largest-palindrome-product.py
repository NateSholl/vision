import numpy as np


#Function Defintion
def is_palindrome(num):

    #Convert number to string
    some_string = str(num)

    #If string is same forward and backwards
    if some_string == some_string[::-1]:
        return True
    else:
        return False

palin_list= []
#for loop 
for i in range(1,999):

    for j in range(1,999):

        
        #Calculate product of 3-digit number
        product = (999 - j) * (999 - i)

        if is_palindrome(product) == True:
             palin_list.append(product)

print(max(palin_list))

