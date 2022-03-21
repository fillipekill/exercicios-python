distancia = float(input('Qual a distância da sua viagem? em km '))

if distancia <= 200:
    print(f'o preço da sua viagem foi R$ {distancia * 0.50:.2f}')
else:
    print(f'o preço da sua viagem foi R$ {distancia * 0.45:.2f}')