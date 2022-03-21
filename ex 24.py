nome = input ('Poderia me falar o seu nome completo? ')
lista = nome.split()
primeiro = lista[0]
ultima = lista[len(lista) - 1]

print (f'seu primeiro nome é {primeiro} e o seu ultimo nome é {ultima}')