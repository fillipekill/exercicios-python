lista = []

for i in range(5):
    num = int(input('Poderia me dar um número? '))

    if i == 0 or num > lista[-1]:
        lista.append(num)

    else:
        for pos,item in enumerate(lista):
            
            if num <= item:
                lista.insert(pos,num)
                break


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
