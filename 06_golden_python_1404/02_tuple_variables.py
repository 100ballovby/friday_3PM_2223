age = height = weight = 20  # трамвайное присваивание - это когда вы присваиваете нескольким переменным одно значение

print(age)
print(height)
print(weight)

i = 6; j = 12; k = 19  # так присваивать тоже можно, но не нужно

length, height, depth = 21, 16, 8
# кортеж переменных - это одновременное присваивание разных значений разным переменным
peoples = ['Mary Jane', 'John Parker', 'Louis Carol', 'Alice Ford']
tuple_peoples = []  # [('name', 'surname'), ('name', 'surname'), ('name', 'surname'), ('name', 'surname')]
for people in peoples:
    name, surname = people.split()  # первый элемент списка уйдет в name, второй в surname
    tuple_peoples.append((name, surname))

print(tuple_peoples)

# обмен значений переменных
x = 5
y = 3
tmp = x  # 5
x = y  # 3
y = tmp  # 5
print(x, y)

# обмен значений через кортеж
x = 5
y = 3
x, y = y, x
print(f'x = {x}')
print(f'y = {y}')

