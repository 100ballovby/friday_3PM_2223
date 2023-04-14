def say_hello(name, age, country):  # определение функции
    return f"Hello, {name}! You're {age} yo, and living in {country}"  # функция должна возвращать результат своей работы


# функция не работает, не создается и не существует до момента, пока вы ее не вызовите
greeting = say_hello('Demid', 13, 'Norway')  # значений, которые передаются функции, может быть сколько угодно
# в переменную greeting ВОЗВРАЩАЕТСЯ строка из функции
print(greeting)



