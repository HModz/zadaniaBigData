# szyfrowanie pliku tekstowego szyfrem Cezara

ilosc_przesuniec = int(input("Podaj liczbę przesuniec: "))

tekst = open("tekst.txt", "r")
tekst = tekst.read()

zaszyfrowany = open("zaszyfrowany.txt", "w+")

lista = []
nowe_slowo = []

for i in range(0,len(tekst)):
    litera = ord(tekst[i])
    lista.append(litera + ilosc_przesuniec)
    zmiana = chr(lista[i])
    nowe_slowo.append(zmiana)

zaszyfrowany.write("".join(nowe_slowo))
zaszyfrowany.close()
print(tekst)

