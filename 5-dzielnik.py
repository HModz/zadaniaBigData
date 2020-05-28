#dzielniki liczby

liczba = int(input("Podaj liczbę:"))

for i in range(1, liczba+1):
   if liczba % i == 0:
        print(i)