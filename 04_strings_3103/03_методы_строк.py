print(len('абракадабра'))  # узнать длину строки
phrase = 'HeLlO, WoRlD! i am andrew'
print(phrase.upper())  # превести все символы (буквы) в строке в верхний регистр
print(phrase.lower())  # превести все символы (буквы) в строке в нижний регистр
print(phrase.title())  # каждое слово в строке будет написано с большой буквы (слова разделяются пробелами)
print(phrase.capitalize())  # первая буква в первом слове строки будет большой

# методы проверки
print('A is lower: ', 'A'.islower())  # метод проверяет, написан ли СИМВОЛ в нижнем регистре
print('a is upper: ', 'a'.isupper())  # метод проверяет, написан ли СИМВОЛ в верхнем регистре
print('5 is digit: ', '5'.isdigit())  # метод проверяет, является ли СИМВОЛ цифрой
print(f'\0.is printable: ', '\0'.isprintable())  # проверяет, входит ли символ в те символы, что можно набрать на клавиатуре

hello = 'Hello, Andrew!'
if hello.startswith('Hello'):  # проверяет, начинается ли строка с последовательности символов из скобок
    print('Hello!')
else:
    print('Bye bye')

# разбить строчку и превратить ее в список
phrase2 = 'Привет, Андрей! Зачем ты плюнул в голубей?'
word_list = phrase2.split()  # разбивает строку по пробелам и делает каждый элемент элементом списка
print(word_list)
phrase3 = 'Audi,Mercedes,BMW,Opel'
cars = phrase3.split(',')  # split можно передать символ, по которому он будет разбивать строку
print(cars)

print(phrase2.replace('у', '%'))
phrase4 = 'I love C++'
print(phrase4.replace('C++', 'Python'))