def read_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text

def hw():
    numbers = read_file('numbers.txt')
    array = numbers.split()
    for i in range(len(array)):
        array[i] = int(array[i])
    return array

print(hw())
