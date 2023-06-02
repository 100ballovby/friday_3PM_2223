"""
1. Файл для начала работы нужно открыть;
2. Файл нужно обработать (чтение/запись);
3. Файл для сохранности данных в нем необходимо закрыть.
"""
with open('example.txt', 'w') as file:  # file = open('example.txt', 'w') <- открыть файл и сохранить его в переменной
    text = input('Напиши что-нибудь: ')
    file.write(text)
# как только заканчиваются команды с отступом, файл автоматически закрывается
"""
b - binary - данные в виде двоичных последовательностей 
r - read - чтение данных из файла и перевод их в str 
w - write - запись данных в файл (при этом старые данные из файла сотрутся)
r+/w+ - это одновременно чтение и запись или запись и чтение
a - append - это запись данных в файл (при этом старые данные в файле остаются)
"""
with open('example.txt', 'r') as file:
    res = file.read()
    print(f'В файле написано:\n{res}')
