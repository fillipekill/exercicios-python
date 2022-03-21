num = int(input('Poderia me falar quantos termos de uma sequencia de fibonacci você quer ver?'))

first_num = 0
second_num = 1
count = 0

while count < num:
    third_num = second_num + first_num

    print(third_num)

    first_num = second_num
    second_num = third_num

    count += 1