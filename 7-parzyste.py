#ilosc liczb parzystych 1-200

suma = 0

for i in range(1,201):
    if i % 2 == 0:
        print(i)
        suma = suma + 1
print(f"Ilość liczb parzystych: {suma}")