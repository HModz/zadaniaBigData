# sprawdzanie palindromu
from re import sub

def sprawdzaniePalindromu(tekst):
    tekst = sub("[^a-zA-Z]", "", tekst) #usuwanie spacji z tekstu
    tekst = tekst.lower()
    odwrocony = tekst[::-1]

    if (tekst == odwrocony):
        return True
    return False

tekst = input("Podaj wyrazenie do sprawdzenia czy jest palindromem: ")
odpowiedz = sprawdzaniePalindromu(tekst)

if (odpowiedz):
    print("Twoje wyrazenie jest palindromem!")
else:
    print("Twoje wyrazenie nie jest palindromem!")
