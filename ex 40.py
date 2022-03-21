preco = float(input('Poderia falar o preço do produto? '))
pagamento = input('''Qual sera a forma de pagamento?
1 - dinheiro ou cheque com 10 por cento de desconto
2 - vista no cartao com 5 por cento de desconto
3 - até 2x no cartão sem juros
4 - até 3x ou mais no cartão com 20 por cento de juros
''')

if pagamento == '1':
    desconto = preco * (10 / 100)
    print(f'o preço final para ser pago é de R$ {desconto - preco:.2f}')
elif pagamento == '2':
    desconto = preco * (5 / 100)
    print(f'o preço final para ser pago é de R$ {desconto - preco:.2f}')
elif pagamento == '3':
    print('o preço final para ser pago é de R$ {pagamento:.2f}')
elif pagamento == '4':
    juros = preco * (20 / 100)
    print(f'o preço final para ser pago é de R$ {juros + preco:.2f}')
else:
    print('Você inseriu um número inválido, reinicie o programa.')