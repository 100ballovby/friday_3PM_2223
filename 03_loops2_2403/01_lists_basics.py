lst = []  # список
lst1 = [5, 12, 7, 8, 9, 0, -4, 21]
print(type(lst))  # <class 'list'>
print(lst1[3])  # вывести из списка lst1 элемент с индексом 3

# заменить значение третьего элемента списка на число 109
lst1[2] = 109
print(lst1)

# добавить элемент в конец списка
lst1.append(1024)
print(lst1)

# вставить элемент на определенный индекс
lst1.insert(4, 99)  # первый аргумент - это индекс, второй - это число, которое хотим поместить в список
print(lst1)
# lst1[4] = 99 - это замена, поэтому такой синтаксис не используем

# удаление элементов производится с помощью метода .pop(index)
# параметр index позволяет указать, элемент с каким индексом нужно удалить из спика
# если не указать index, удалится последний элемент
lst1.pop(4)  # удалить пятый элемент
print(lst1)
lst1.pop()  # удалить последний элемент
print(lst1)