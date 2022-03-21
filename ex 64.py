from time import sleep as backend_working

total = 0
expensive_products = 0
cheaper_product_name = None
cheaper_product_price = None


while True:
    product_name = input('Qual o nome do produto? ')
    product_price = float(input('Qual o preço deste produto? '))

    total += product_price
    
    if product_price > 1000:
        expensive_products += 1
    
    if cheaper_product_price == None:
        cheaper_product_name = product_name
        cheaper_product_price = product_price
    
    elif product_price < cheaper_product_price:
        cheaper_product_price = product_price
        cheaper_product_name = product_name
    
    option = None
    
    print(f'Anexando os dados...')
    backend_working(0.7)

    while True:
        option = input(f'Você quer continuar? [S/N]')
        
        if option in 'Ss' or option in 'Nn':
            break
    
        print('Digite algo válido')

    if option in 'Nn':
        break
    
    
print(f'o total gasto na compra é de R$ {total:.2f}.')
print(f'o total de produtos que passam de R$ 1000.00 são {expensive_products}.')
print(f'o nome do produto mais barato é {cheaper_product_name} e o seu preço é de R$ {cheaper_product_price:.2f}.')