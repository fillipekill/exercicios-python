list = ('Kit Mouse E Teclado',172.39,
'Mouse Pad',160.89,
'Mouse Gamer',275.55,
'Receptor Usb',49.88,
'Capa C/ Teclado',419.90,
'Webcam C270',164.92,
'Volante G29',1999.90,
'Cx som',140.17)

print('-'*40)
print(f"{'LOJA NEVADOTECH':^40}")
print('-'*40)

for position, item in enumerate(list):
    if position % 2 == 0:
        print(f'{item:.<30}',end= '')

    else:
        print(f'R$ {item:>7.2f}')
