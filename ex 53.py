from random import randint

soma = 1 
num = randint(0,10)

chance = int(input('Sorteamos um número entre 0 e 10, se você acertar ganhará aulas com o professor Nevado.\nQual seu palpite? '))

while chance != num:
    chance = int(input('Seu palpite foi errado, tente outro número. '))
    soma += 1

print(f'Parabéns o número era {num}.\nVocê fez {soma} tentativas.')