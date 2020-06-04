import numpy as np
import time

m = int(input("Podaj M: "))
n = int(input("Podaj N: "))

start = time.time()

macierz1 = np.random.randint(1, 14, (m, n))
macierz2 = np.random.randint(1, 14 , (m, n))
suma = macierz1 + macierz2

print(suma)

print(f"Czas wykonania kodu: {time.time() - start} s")