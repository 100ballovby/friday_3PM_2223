def read_file(filename):
    content = ''
    with open(filename, 'r') as f:
        for line in f.readlines():  # метод формирует список, который состоит из отдельных строк файла
            content += line.strip()  # убираем методом strip пробелы и переносы строки и добавляем к переменной content
    return content


pi = read_file('pi_digits.txt')
pi_million = read_file('pi_million_digits.txt')
print(pi)
print(len(pi_million))
pi_num = float(pi)
print(pi_num)


