s = ''  # <class 'str'>
s1 = "hello"  # <class 'str'>
s2 = input('Введи что-то: ')
print(s1[0])  # вывести символ с индексом 0 из строки s1

for i in range(len(s1)):
    print(s1[i], end=' ')

print()
print(s2)
