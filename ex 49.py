from datetime import date

ano_atual = date.today().year
pessoas_maiores = 0


for i in range(0, 7):
    ano = int(input('Poderia me falar o seu ano de nascimento? '))
    idade = ano_atual - ano
    if idade >= 18:
        pessoas_maiores += 1
print(f'De todas pessoas, {pessoas_maiores} são maior(es) de idade. E o número de pessoas menor(es) de idade são {7 - pessoas_maiores}.')
