def write_file(filename, text):
    with open(filename, 'w') as f:
        f.write(text)


def read_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text


write_file('written.txt', 'There is some text')
print(read_file('written.txt'))

