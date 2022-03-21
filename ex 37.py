idade = int(input('Quantos anos você tem? '))

if idade <= 9:
    print('Você é um aluno Mirim')
elif idade <= 14:
    print('Você é um aluno Infantil')
elif idade <= 19:
    print('Você é um aluno Junior')
elif idade <= 20:
    print('Você é um aluno Sênior')
else:
    print('Você é um aluno Master')