name = input('Bom dia, qual seu nome? ')
casa = float(input(f'{name} pro seu empréstimo ser aceito precisamos de algumas informações\nQual o valor da casa? '))
salario = float(input('Qual o valor do seu salário? '))
anos = float(input('Em quantos anos você pretende pagar? '))
trinta = salario * (30 / 100)
parcela = casa / (12 * anos)

if parcela < trinta:
    print(f'{name} parabéns, seu salário foi aceito, você vai pagar {parcela:.1f} reais por mês')
else:
    print ('Não conseguimos efetivar o seu empréstimo o valor 30 por cento do seu salário')
