etalon = input("Insert symbol: ")
char = ""  # переменная, в которую буду сохранять символы из ввода пользователя
string = ""  # переменная, в которой хранится итоговая строка

while ((char.lower() != etalon) and (char.upper() != etalon)):
    """В условии задачи сказано, что ввод нужно прекратить, как только
    будет встречен эталонный символ. Так как его могут ввести либо
    в нижнем регистре (маленькая буква), либо в верхнем (большая буква),
    программа должна проверить оба варианта исхода. Для этого
    нам нужна операция ИЛИ"""
    char = input("Insert letter or punctuation: ")
    if (len(char) > 1):  # если длина значения переменной char больше 1
        print("There is only one symbol allowed!")
    else:  # если длина значения переменной char равна 1
        string += char  # добавляю к строке символ

print(string)

