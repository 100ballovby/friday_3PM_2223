import random as r


def file_to_list(filename):
    content = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if line.strip():  # если строка не пустая (пустая строчка - это False)
                content.append(line.strip())
    return content


alice = file_to_list('alice.txt')
lines = {}
for i in range(len(alice)):
    lines[i] = len(alice[i].split())
print(lines)

finish = False
while not finish:
    ans = input('Хочешь получить случайную строчку из "Алисы в стране чудес"? (y/n): ')

    if ans.lower() == 'y':
        print(r.choice(alice))
    else:
        print('Ok, bye!')
        finish = True


