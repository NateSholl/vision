list = [1,2]
i = 0
sum_of_evens = 0

while i <= 4000000:
    list.append(list[-1] + list[-2])
    i = list[-1]
    
for x in list[0:-1]:
    if x % 2 == 0:
        sum_of_evens += x

print(sum_of_evens)
