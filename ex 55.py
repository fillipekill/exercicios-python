num = int(input('Poderia me dar um número? '))
factorial = None

while num != 1:
    if factorial == None:
        factorial = num
    else: 
        factorial *= num

    num -= 1

print(f'o factorial do seu número é: {factorial}')