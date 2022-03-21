menor = None
maior = None

for i in range(0,5):
    peso = float(input('Poderia me falar o seu peso? '))
    if menor is None:
        menor = peso
    
    if maior is None:
        maior = peso

    if peso >= maior:
        maior = peso

    if peso <= menor:
        menor = peso

print(f'o menor peso foi de {menor} e o maior peso foi de {maior}')