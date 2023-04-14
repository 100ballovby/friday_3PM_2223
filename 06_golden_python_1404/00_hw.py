input = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla vel aliquet ex, in porta orci. Vestibulum at leo finibus, vulputate diam a, sagittis sem. Donec a nibh ac sem convallis dignissim vitae vel sapien.'
output = ''

for i in range(len(input)):
    if i % 2 != 0:
        output += input[i]

print('убрали четные индексы:')
print(output)



