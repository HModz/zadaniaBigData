# przekształcanie liczb na system binarny

liczba = int(input("Podaj liczbę: "))
dwa = 2
def Binarna(x):
        if x > 0:
            Binarna(x // 2)
            print(x % 2, end="")

Binarna(x=liczba)