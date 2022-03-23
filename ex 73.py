lista = []

for i in range(5):
    num = int(input('Poderia me dar um número? '))
    lista.append(num)

lista.sort()

print(f'o menor número da lista é: {lista[0]}\nO maior é: {lista[-1]}')








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