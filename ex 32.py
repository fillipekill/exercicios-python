um = float(input('Poderia me  dar o valor de uma reta? '))
dois = float(input('Poderia me  dar o valor de outra reta? '))
tres = float(input('Poderia me  dar o valor de outra reta? '))

if um < dois:
    if um < tres:
        menor_de_todos = um
        if dois < tres:
            segundo_menor = dois
            maior = tres
        else:
            segundo_menor = tres
            maior = dois

if dois < um:
    if dois < tres:
        menor_de_todos = dois
        if tres < um:
            segundo_menor = tres
            maior = um
        else:
            segundo_menor = um
            maior = tres

if tres < dois:
    if tres < um:
        menor_de_todos = tres
        if dois < um:
            segundo_menor = dois 
            maior = um
        else:
            segundo_menor = um
            maior = dois

if maior < (segundo_menor + menor_de_todos):
    print('O comprimento das retas que você me deu resultou em um triângulo')
else:
    print('O comprimento das retas que você me deu não resultou em um triângulo')