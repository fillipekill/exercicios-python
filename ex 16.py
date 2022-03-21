#COMO CALCULAR O TEOREMA DE PITÁGORAS


from math import sqrt

cateto_oposto = int(input('Poderia me dar o valor do cateto oposto de um triângulo retângulo? '))
cateto_adjacente = int(input('Poderia me dar o valor do cateto adjacente de um triângulo retângulo? '))

print(f'o valor da soma é {sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2):.0f}')