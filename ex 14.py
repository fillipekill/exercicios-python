#Calcular quantidade de dias e quilômetros rodados por um carro alugado.


quantidade_km = float(input('Bom dia, qual foi a quantidade de quilômetros percorridos com o carro? '))
quantidade_dias = int(input('e qual a quantidade de dias que você usou o carro? '))
resultado_dias = quantidade_dias * 60 
resultado_km = quantidade_km * 0.15
resultado = resultado_km + resultado_dias

print(f'o preço a pagar pelo uso do carro será:{resultado} ')