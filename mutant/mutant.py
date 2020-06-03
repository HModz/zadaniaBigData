# MUTANT
import random
import string


def Mutant():
    lista = open("mutant.txt", "w+")

    for i in range(1, 301, 1):
        lista.write(''.join(random.choice(string.ascii_uppercase) for x in range(50)))
        lista.write("\n")
    lista.close()

    lista = open("mutant.txt", "r")
    tekst = lista.read().splitlines()

    for i in range(0, len(tekst)):
        print(tekst[i])
        print(f"Suma znaków ASCII:{sum(ord(ch) for ch in tekst[i])}")
    lista.close()

Mutant()