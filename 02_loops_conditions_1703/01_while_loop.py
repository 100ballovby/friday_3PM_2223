num = eval(input('Insert number: '))

while (num > 0):
    if ((num % 2) == 0):  # если число четное (остаток от деления на 2 равен 0)
        print('Divide by two:')
        num /= 2
        print(num)
    else:
        print('Different with one:')
        num -= 1
        print(num)
