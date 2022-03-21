first_value = int(input('Poderia me dar um número? '))
second_value = int(input('Poderia me dar outro número? '))
escolha = None

while escolha != 5:
    escolha = int(input('''Temos 5 opções
[1] irei somar os números
[2] irei multiplicar os números
[3] irei mostrar qual é o maior número
[4] você vai substituir os número que temos
[5] você sai do programa
O que você escolhe? 
'''))
    
    if escolha == 1:
        print(f'a soma dos valores são {first_value + second_value}')
    
    elif escolha == 2:
        print(f'a multiplicação dos números resulta em: {first_value * second_value}')
    
    elif escolha == 3:
        if first_value < second_value:
            print(f'{second_value} é o maior número')
        else:
            print(f'{first_value} é o maior número')

    elif escolha == 4:
        first_value = int(input('Qual será o novo primeiro número? '))
        second_value = int(input('Qual será o novo segundo número?'))

    elif escolha == 5:
        print('Saindo do programa...')
    
    else: 
        print('Digita algo válido PAU NO ARO')