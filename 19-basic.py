import random
import time

n = int(input("Podaj M: "))
m = int(input("Podaj N: "))

start = time.time()

m1 = []
m2 = []
s = []
for w in range(n):
    kol1 = []
    kol2 = []
    kols = []
    for k in range(m):
        x = random.randint(1, 14)
        y = random.randint(1, 14)
        z = x + y
        kol1.append(x)
        kol2.append(y)
        kols.append(z)
    m1.append(kol1)
    m2.append(kol2)
    s.append(kols)

for macierz1 in m1:
    print(str(macierz1))
print("\n")
for macierz2 in m2:
    print(str(macierz2))
print("Suma:")
for suma in s:
    print(str(suma))
print(f"Czas wykonania kodu: {time.time() - start} s")
