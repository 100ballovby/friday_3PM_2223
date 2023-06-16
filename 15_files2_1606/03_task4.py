def read_file(filename):
    with open(filename, 'r') as f:
        text = f.read().split()
    return text

sid = read_file('siddhartha.txt')

with open('output.txt', 'w') as file:
    for word in sid:
        file.write(word.upper() + '\n')



