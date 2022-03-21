fifty = 0
twoenty = 0
ten = 0
one = 0

price = int(input('Banco Nevado.\nQuanto você deseja sacar? '))

while price > 0:
    
    if price >= 50:
        price -= 50
        fifty += 1
    
    elif price >= 20:
        price -= 20
        twoenty += 1
    
    elif price >= 10:
        price -= 10
        ten += 1
    
    elif price >= 1:
        price -= 1
        one += 1

print(f'Você receberá {fifty} cédulas de R$50')
print(f'Você receberá {twoenty} cédulas de R$20')
print(f'Você receberá {ten} cédulas de R$10')
print(f'Você receberá {one} moedas de R$1')
