

from sqlalchemy import true


def is_prime(num):
    for i in range(2,int(num/2)):
        if num % i == 0:
            return False
    return True

def largest_factor(num):
    running = True
    while running == True:
        x = 0
        for i in range(2,num):
            if int(num / i) == num / i and is_prime(num / i) == True: 
                x = i
                running = False
                break
    return num / i 

print(largest_factor(600851475143))

