sexo = input('Poderia me falar o seu sexo? [M/F] ').upper().strip()


while not sexo in 'MF':
    sexo = input('Coloque um sexo válido ').upper().strip()

print(f'seu sexo é {sexo}')