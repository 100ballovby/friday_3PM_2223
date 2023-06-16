def write_file(filename, text_list):
    with open(filename, 'w') as f:
        if type(text_list) == list:
            for line in text_list:
                f.write(line + '\n')
        else:
            f.write(text_list)


def read_file(filename):
    res = []
    with open(filename, 'r') as f:
        text = f.readlines()
        for line in text:
            if line.strip():  # если строка с примененным strip() не пустая
                res.append(line.strip())  # записать эту строку в список
    return res


text = read_file('siddhartha.txt')
print(text)
text.reverse()
write_file('output.txt', text)
write_file('res2.txt', 'lgkfglj;lreknrf wcrrelkrglfkmqre,jgjfpo3krwnef,vw er;ofjn2 4wrgpof2k3e')

# task 1
write_file(input('название файла: '), input('текст: '))

