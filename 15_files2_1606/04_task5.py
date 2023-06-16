file1 = input('filename 1: ')
file2 = input('filename 2: ')


def read_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text


res = read_file(file1)
res2 = read_file(file2)
print(f'информация в файлах одинакова: {res == res2}')


