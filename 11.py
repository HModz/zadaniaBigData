#ilosc liczb mniejszych od 23 w liscie 100 elementow
#nie wiem czy dobrze zrozumialem polecenie ale nie ma w nim ograniczenia przedialu losowego wiec zastosowalem do 1000

import random

x = 0
lista = random.sample(range(0,1000),100)
print(lista)

for i in range(0,len(lista)):
    if lista[i] < 23:
        x = x + 1
print(x)