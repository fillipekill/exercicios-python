resultado = 0
soma = 0

while True:
    num = int(input('Digite um número '))
    
    if num == 999:
        break

    resultado += num
    soma += 1

print(f'Você digitou {soma} números e a soma deles é {resultado}')