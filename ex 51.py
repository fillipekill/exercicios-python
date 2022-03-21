idade_soma = 0
mais_velho = None
nome_velho = None
femeas = 0

for i in range(0,4):
    nome = input('Poderia me falar o seu nome? ')
    idade = int(input('Poderia me falar a sua idade? '))
    sexo = input('Poderia me falar o seu sexo? ')
    
    idade_soma += idade

    if sexo.lower() == 'masculino' or sexo.lower() == 'm':
        
        if mais_velho == None:
            mais_velho = idade
            nome_velho = nome
        
        if idade >= mais_velho:
            mais_velho = idade
            nome_velho = nome
   
    else:    
        if idade > 20:
            femeas += 1

media = idade_soma / 4

print(f'''
A média de idade do grupo é: {media}
o nome do homem mais velho é:{nome_velho} 
Quantas mulheres têm mais de 20 anos {femeas}''')