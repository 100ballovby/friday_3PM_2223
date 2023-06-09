import os


entries = os.listdir(os.path.dirname(__file__))  # формирует список из всего содержимого папки, в которой запускается файл
print(entries)

with open('test.txt', 'w') as f:
    f.write(*entries)


