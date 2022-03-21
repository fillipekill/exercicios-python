primeiro_termo = int(input('Poderia me dar o primeiro termo de uma progressão aritmética? '))
razao = int(input('Qual será a razão dessa progressão aritmética? '))

count = 10
termo_atual = primeiro_termo

while count > 0:
    print(f'{termo_atual}')
    termo_atual += razao
    count -= 1

    if count == 0:
        count = int(input('Quantos termos mais vc deseja: '))
