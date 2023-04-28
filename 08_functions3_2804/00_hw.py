def task_1(name):
    address = f'{name}\nBelarus, Minsk, 220080, krasnaya, 7A'
    print(address)


def task_2(price, tax):
    res = price + (price * tax / 100)
    print(res)

task_1('Demid Raksin')
task_2(19362, 4)
