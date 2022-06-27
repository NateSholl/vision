
import math

def is_prime(num):
    if num == 2:
        return True
    else:
        for i in range(2,math.ceil(math.sqrt(num)+1)):
            if num % i == 0:
                return False
    return True


inputNum = 10001
check = 0
x = 1

while check < inputNum:
  
    x += 1
    if is_prime(x) == True:
        check += 1
    
print(x)
        
