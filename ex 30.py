one, two, three = float(input('Poderia me dar um número? ')), float(input('Poderia me dar outro numero? ')), float(input('Poderia me dar outro numero? '))

if one >= two and one >= three:
    maior = one

if two >= three and two >= one:
    maior = two

if three >= two and two >= one:
    maior = three

if one <= two and one <= three:
    menor = one

if two <= three and two <= one:
    menor = two

if three <= two and three <= one:
    menor = three

print(f"Maior: {maior}, Menor: {menor}")
