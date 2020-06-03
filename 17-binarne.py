# przekształcanie liczb na system binarny

liczba = int(input("Podaj liczbę: "))

def Binarna(x):
        if x > 0:
            Binarna(x // 2)
            print(x % 2, end="")

Binarna(liczba)