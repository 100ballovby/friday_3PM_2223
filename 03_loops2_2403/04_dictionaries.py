""" Словарь - это коллекция данных, в которой хранятся пары ключ:значение.
Индексы в словарях отстутствуют, вместо них используются ключ, которые, как правило,
задаются человеком/алгоритмом, который создает этот словарь. """

grocery = {
    'cookies': 4.56,
    'orange': 1.23,
    'apple': 4.52,
    'grape': 9.43,
    'milk': 5.33,
    # ключи в словарях не могут повторяться, если вы так сделаете, то значением будет то, что стоит по списку ниже
    # 'cookies': 2.33 <- значение ключа cookies будет 2.33, а не 4.56
}
print(grocery)
# замена значения в словаре производится через подстановку нового значения ключу
grocery['milk'] = 3.22  # вместо индекса ставим название ключа
print(grocery)
# обращаться к ключам, которых нет, нельзя. Получите ошибку KeyError
# print(grocery['banana'])

# добавить новую пару ключ-значение, то пишем так:
grocery['banana'] = 19.45  # если добавить к несуществующему ключу значение, вы добавите новую пару
print(grocery)

# удалять из словаря можно только пары
del grocery['orange']  # делать это можно, но не нужно
print(grocery)

# чтобы перебрать ключи, используем метод .keys()
for key in grocery.keys():
    print('ключ:', key, ', значение:', grocery[key])

# чтобы перебрать значения, используем метод .values()
for value in grocery.values():
    print('значение ', value)

# чтобы перебрать сразу и ключи, и значения, используем метод items с двумя управляющими переменными цикла for
for key, value in grocery.items():
    print(key, ':', value)

