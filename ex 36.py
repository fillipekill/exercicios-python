etapa_one = float(input('Nevado deu as notas de Python\nQuanto você tirou na primera etapa? '))
etapa_two = float(input('E na segunda etapa? ' ))
etapa_three = float(input('E na Terceira etapa? '))
multi_etapa_1 = etapa_one * 3 
multi_etapa_2 = etapa_two * 3
multi_etapa_3 = etapa_three * 4
num = multi_etapa_1 + multi_etapa_2 + multi_etapa_3
num2 = num / 10

if num2 < 5:
    print('Você perdeu de ano em Python com o professor Nevado.')
elif num2 < 7:
    print('Você está de recuperação com o professor Nevado.')
else:
    print('Parabéns, você passou em Python com o professor Nevado.')

#1 NOTA PESA 3
#2 NOTA PESA 3
#3 NOTA PESA 4
#FOMULA: CADA ETAPA MULTIPLICADA PELO SEU PESO, A SOMA DE CADA ETAPA MULTIPLICADA PELO SEU PESO, DIVIDE PELA SOMA DOS PESOS