import random

x = 8
y = 6

randtotal = 0
die_set = []
for i in range(x):
    print(randtotal)
    die_val = random.randint(1,y) 
    randtotal += die_val
    die_set.append(die_val)
    print('i',i)
print('total:',randtotal)
print(die_set)
