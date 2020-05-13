#szyfr +1

slowo = input("Wpisz tekst: ")
lista = []
nowe_slowo = []
for i in range(0,len(slowo)):
    litera = ord(slowo[i])
    lista.append(litera + 1)
    zmiana = chr(lista[i])
    nowe_slowo.append(zmiana)

print ("".join(nowe_slowo))

