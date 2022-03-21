while True:
    num = int(input('Digite um número '))
    
    if num < 0 :
        break
    
    count = 1

    while count < 11:
        print(f'{num} X {count} = {num * count}')
        
        count += 1