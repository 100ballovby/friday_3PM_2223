# нужно написать функцию, которая определяет, есть ли в строке, переданной через аргумент, пробелы
def have_spaces(string: str) -> bool:
    """
    Функция определяет наличие пробелов в строке
    :param string: Строка для проверки
    :return: логический результат проверки
    """
    return ' ' in string


strings = ['hello,', 'China', ' jjj', 'hi there', 'call_the_police', 'find_spaces in_me']
for string in strings:
    print(f'{string} has spaces: {have_spaces(string)}')


