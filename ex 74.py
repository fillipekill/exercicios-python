from time import sleep

lista = []

while True:
    num = int(input('Digite um número '))
    option = input('Quer continuar? [S/N]')
    
    if num not in lista:
        lista.append(num)
        print('Anexando...')
        sleep(0.5)
        print('Número adcionado com sucesso')
    
    else:
        sleep(0.5)
        print('Número duplicado, não foi anexado.')
    
    if option in 'Nn':
        break    

lista.sort()

print(lista)





# Listas

# Add elements 
# .append(value)
# .insert(index, value)

# Remove elements
# del list[index]
# list.pop(index?)
# list.remove(value)

# Declare List
# list(*args)
# list(range(start, end))

# Utils
# list.sort(reverse?= boolean)
# len(list)