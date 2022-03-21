primeiro_termo = float(input('Poderia me dar o primeiro termo de uma progressão aritmética? '))
razao = float(input('Qual será a razão dessa progressão aritmética? '))

for i in range(0,10):
    print(f'{primeiro_termo + i * razao:.0f}')
