import random

a = random.randint(1, 20)
# хочу проверить, принадлежит ли число а промежутку [1;15]
if ((a >= 1) and (a <= 15)):
    print(a, 'принадлежит')
else:
    print(a, 'не принадлежит')


