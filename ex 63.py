from time import sleep

dezoitou = 0
man = 0
woman = 0


while True:
    age = int(input('Qual sua idade? '))
    sex = input('Qual seu sexo? [F/M] ')

    if age > 18:
        dezoitou += 1
    
    if sex in 'Mm':
        man += 1
    
    else:
        if age < 20:
            woman += 1
    
    print('Anexando os dados!')
    sleep(0.5)
    option = input('Você quer continuar a contagem? [S/N] ')
    
    if option in 'Ss':
        continue
    break


print(f'Com os dados que você me deu, temos {dezoitou} pessoas maiores de 18 anos.')
print(f'Temos {man} homens.')
print(f'Temos {woman} mulheres menores de 20 anos')