import emoji
import random

opcao = int(input(emoji.emojize('''Vamos jogar jokenpô?
Escolha uma das opções:

  1 - Pedra :punho_direito:
  2 - Papel :mão_levantada:
  3 - Tesoura :mão_em_v_de_vitória:
''', language='pt')))

pedra = 1
papel = 2
tesoura = 3

computador = random.randint(1, 3)


if computador == opcao:
    print('Deu empate!')

elif opcao == pedra and computador == papel:
    print('Você perdeu, eu joguei papel.')

elif opcao == pedra and computador == tesoura:
    print('Você ganhou, eu joguei tesoura.')

elif opcao == papel and computador == pedra:
    print('Você ganhou, eu joguei pedra')

elif opcao == papel and computador == tesoura:
    print('Você perdeu, eu joguei tesoura ')

elif opcao == tesoura and computador == papel:
    print('Você ganhou, eu joguei papel.')

elif opcao == tesoura and computador == pedra:
    print('Você perdeu, eu joguei pedra.')