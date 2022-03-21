#Como calcular a área e descobrir quantos litros deve se usar para preencher essa área


largura = float(input('Bom dia, poderia me dar a largura de uma parede? Obs: a medida deve ser em metros '))
altura = float(input('Poderia me informar uma altura? obs: a medida deve ser em metros '))

print(f'{largura *altura:.0f} metros é área da parede, com isso temos que será necessario {largura *altura / 2:.0f} litros de tinta')