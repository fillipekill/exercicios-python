resultado = 0
soma = 0
num = None

while num != 999:
    num = int(input('Digite um número '))
    if num != 999:
        resultado += num
        soma += 1

print(f'Você digitou {soma} número(s).\nO resultado dos números que você digitou é {resultado}')