numero = (int(input('poderia me dar algum numero de 0 a 9999?')))

milhares = numero // 1000 % 10
centenas = numero // 100 % 10
dezenas = numero // 10 % 10
unidades = numero % 10

print(f'Seu número teve {unidades} unidades, {dezenas} dezenas, {centenas} centenas, {milhares} milhares')