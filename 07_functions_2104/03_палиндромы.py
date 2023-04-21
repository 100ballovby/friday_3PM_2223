words = ['шалаш', 'имамами', 'level', 'evil',
         'довод', 'сос', 'orange', 'водоходов',
         'балабол', 'лабрадор', 'казак', 'заказ']


def is_palindrome(word: str) -> bool:
    return word[::] == word[::-1]


for word in words:
    print(f'{word} is palindrome: {is_palindrome(word)}')

