salario = float(input('Qual o valor do seu salário? '))
aumento_10 = salario * (10 / 100)
aumento_15 = salario * (15 / 100)
6
if salario >= 1250.00:
    print(f'o seu novo salario é {salario + aumento_10} você recebeu 10 % de desconto, pois seu salario era maior que 1250.00')
else:
    print(f'o seu novo salario é {salario + aumento_15} você recebeu 15 % de desconto, pois seu salario era menor que 1250.00')
    