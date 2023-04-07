phrase = input('впиши строчку: ')
count = 0

for i in range(len(phrase)):
    if phrase[i] in ',.!?;:-':
        count += 1
print(f'количество знаков: {count}')


