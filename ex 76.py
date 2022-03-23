count = 0
lista = []


while True:
    num = int(input('Digite um número '))
    lista.append(num)
    count += 1

    option = input('Quer continuar? [S/N]')



    if option in 'Nn':
        break  

lista.sort()

print(lista)

print(f'Você digitou:{count} números')

if 5 in lista:
    print('sua lista tem o valor 5')

else: 
    print('Não tem o número 5 na sua lista')




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