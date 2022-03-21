velocidade = float(input('Qual a velocidade que o seu carro está? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'você foi multado o valor da multa foi de {multa} kwanzas!')
else:
    print('Parabéns, você está dentro das leis de trânsito brasileiras.')