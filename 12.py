#suma skladowych krotki do kwadratu

krotka = (1, 3, 5, 6, 3, 5, 6, 1, 3, 85, 96, 1, 5, 123, 456, 8674)
x = 0

for i in range(0,len(krotka)):
    x = x + krotka[i]**2
    
print(x)
