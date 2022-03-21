#Como arrendodar algum número, sem a casa decimal.


from math import trunc 

numero = float(input('Poderia me dar algum número real? '))
print (f'o seu numero arrendodado é: {trunc(numero)}')
