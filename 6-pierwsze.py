#liczby pierwsze

for liczba in range(2,101):
    x = 0
    for i in range(2,liczba//2 + 1):
        if liczba % i == 0:
            x = x + 1
    if x == 0:
        print(liczba)