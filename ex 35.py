from datetime import date

nascimento = int(input('Poderia me falar o ano em que você nasceu? '))
ano_atual = date.today().year
idade = ano_atual - nascimento
if idade > 18:
    print(f'ja passou o tempo de você se alistar no exército brasileiro. Você deveria se alistar há {(idade - 18)} anos')
elif idade == 18:
    print(f'Está na hora de você se alistar. Você possui 18 anos')
else:
    print(f'Quando completar 18 anos poderá se alistar no Exercito Brasileiro. Ainda faltam {18 - idade} anos')