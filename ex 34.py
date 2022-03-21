num1 = int(input('Poderia me dar um número inteiro? '))
num2 = int(input('Poderia me dar outro número inteiro? '))

if num1 > num2:
    print(f'O número {num1} é maior que o {num2}')
elif num2 > num1:
    print(f'o número {num2} é maior que o {num1}')
elif num2 == num1:
    print(f'os números são iguais') 