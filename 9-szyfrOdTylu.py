#szyfr od tylu

tekst = input("Podaj tekst: ")

for i in range(len(tekst),0,-1):
    nowy_tekst = tekst[::-1]

print(nowy_tekst)