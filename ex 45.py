soma = 0

for i in range(0,6):
    num = int(input('Poderia me dar um número?'))
    if num % 2 == 0:
        soma += num

print(soma)