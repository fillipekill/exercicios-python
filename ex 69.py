num1 = int(input('Poderia me dar um número? '))
num2 = int(input('Poderia me dar um número? '))
num3 = int(input('Poderia me dar um número? '))
num4 = int(input('Poderia me dar um número? '))

tuple = (num1,num2,num3,num4)

print(f'Você digitou o número 9 {tuple.count(9)} vezes.')

if 3 in tuple:
    print(f'O número 3 está na posição {tuple.index(3) + 1}')

print(f'Os números pares são:', end=' ')

for i in range(0, len(tuple)):
    
    if tuple[i] % 2 == 0:
        print(tuple[i], end=' ')