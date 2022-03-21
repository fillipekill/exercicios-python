altura = float(input('Poderia me falar a sua altura? '))
peso = float(input('Poderia me falar o seu peso? '))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'o seu imc foi de {imc:.1f} Você está abaixo do peso')
elif imc > 18.5 and imc < 25:
    print(f'o seu imc foi de {imc:.1f} Você está no peso ideal')
elif imc > 25 and imc < 30:
    print(f'o seu imc foi de {imc:.1f} Você está em sobrepeso.')
elif imc > 30 and imc < 40:
    print(f'o seu imc foi de {imc:.1f} Você está na obesidade.')
else: print(f'o imc foi acima de 40, você está em obesidade mórbida.')