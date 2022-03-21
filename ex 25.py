from random import randint

num = randint(0, 5)
user_num = int(input('Poderia me falar algum numero entr 0 e 5? vou sortear algum e se der o seu, vc ganha 5 aulas gratuitas com Kelvin Nevado! '))
if user_num == num:
    print(f'o numero sorteado foi {num} parabéns, você ganhou 5 aulas com Kelvin Nevado!')

else:
    print(f'o numero sorteado foi {num} que pena, tente denovo depois.')                            