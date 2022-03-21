from operator import truediv
from random import randint

victories = 0
num = randint(0,5)

while True:
    par_and_impar = str(input('Vamos jogar par ou ímpar. Você escolhe par ou ímpar? [P/I] '))
    pessoa = int(input('Qual número você escolhe? '))
    
    if par_and_impar in 'Pp':
        if (pessoa + num) % 2 == 0:
            victories += 1
            print(f'Você ganhou, eu joguei {num} e você {pessoa} a soma deu {pessoa + num}\nVamos jogar novamente.')
        else:
            print(f'Você perdeu, eu joguei {num} e você jogou {pessoa} a soma deu {pessoa + num}\nVocê ganhou {victories} vezes.')
            break 
    else:
        if (pessoa + num) % 2 != 0:
            print(f'Você ganhou, eu joguei {num} e você {pessoa} a soma deu {pessoa + num}.\nVamos jogar novamente')
            victories += 1
        else:
            print(f'Você perdeu, eu joguei {num} e você jogou {pessoa} a soma deu {pessoa + num}\nVocê ganhou {victories} vezes.')    
            break
    