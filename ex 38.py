from sexo import is_triangulo
um = int(input('Poderia me dar o valor de uma reta? '))
dois = int(input('Poderia me dar o valor de outra reta? '))
tres = int(input('Poderia me dar o valor de outra reta? '))

triangulo = is_triangulo(um, dois, tres)
if triangulo:
    print('Os valores de reta que você me deu, resulta em um triângulo.')
    if um == dois and um == tres:
        print('Com as retas que você me deu, resulta em um triângulo equilátero')
    
    elif um == dois or um == tres:
        print('Com as retas que você , resulta em um triângulo isósceles.')
    else:
        print('Com as retas que você me deu, resulta em um triângulo escaleno.')
else:
    print('Os valores de reta que você me deu, não resulta em um triângulo')