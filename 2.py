zasoby = float(input("Podaj ilość gotówki: "))
cena_iphone = 1500
szt = zasoby // cena_iphone
reszta = zasoby - cena_iphone*szt

if cena_iphone > zasoby:
    print(f"Brakuje ci jeszcze {cena_iphone - zasoby} zł")
else:
    print(f"Możesz kupić {szt} szt. iphone'a do kolejnego brakuje ci {cena_iphone - reszta} zł")