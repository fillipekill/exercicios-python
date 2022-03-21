num = int(input('Poderia me dar algum numero inteiro? '))

divisiveis = 0

for i in range(num,0, -1):
    if num % i == 0:
        divisiveis += 1
if divisiveis > 2:
    print('O  seu número não é primo.')

else:
    print('O seu número é primo.') 