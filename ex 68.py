from random import randint

num = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

for i in num:   
    print(i,end=' ')

organizado = sorted(num)

print('\n')
print(organizado[0])
print(organizado[-1])