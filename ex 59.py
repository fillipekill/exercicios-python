resposta = 'S'

media = 0
soma = 0
count = 0
menor = 0
maior = 0


while resposta in 'Ss':
    num = int(input('Digite um número '))
    soma += num
    count += 1 

    if count == 1:
        maior = num
        menor = num
    
    else:
    
        if num >= maior:
            maior = num
        
        if num <= menor:
            menor = num

    resposta = input('Quer continuar? [S/N]').upper().strip()
media = soma / count
print(f'Você digitou {count} números e a média entre eles é {media}')
print(f'o maior número foi {maior} e o menor número foi {menor}')