from datetime import date

ano_atual = date.today().year
ano = int(input('Poderia me falar algum ano? '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano que você digitou é bisexual')
else: print('o ano que você digitou não é bisexual')

if ano_atual % 4 == 0 and ano_atual % 100 != 0 or ano_atual % 400 == 0:
    print('Estamos em um ano bisexual')
else: print('Não estamos em um ano bisexual')