import random

def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


tickets = {}
lst = read_file('questions.txt')
for i in range(1, 31):
    tickets[i] = [random.choice(lst), random.choice(lst)]

for key in tickets:
    print(f'Билет №{key}\nВопрос 1: {tickets[key][0].strip()}\nВопрос 2: {tickets[key][1].strip()}')

