#liczby trojkatne z listy 50 liczb z przedzialu 1-1000

import random

lista = sorted(random.sample(range(0, 1000), 50))
triangle = []


def Trojkatne():
    for i in range(1, 100, 1):
        x = ((i ** 2) + i) / (2)
        if x <= 1000:
            triangle.append(x)
        else:
            break

    print(set(lista).intersection(triangle))

Trojkatne()