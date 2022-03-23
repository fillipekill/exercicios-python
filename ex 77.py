lista = []

while True:
    num = int(input('Digite um número '))
    lista.append(num)

    option = input('Quer continuar? [S/N]')

    if option in 'Nn':
        break  

even_numbers = []
odd_numbers = []

for i in lista:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print(f'A primeira lista de números são {lista}\nOs números pares são: {even_numbers} e os ímpares são: {odd_numbers}')




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