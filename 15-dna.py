# obliczanie procentu występowania C + G w kodzie DNA

dna = open("dna.txt", "r")
dna = dna.read()

ilosc_cg = dna.count("C") + dna.count("G")
procent = ilosc_cg / len(dna) * 100

print(f"Procentowy udział C i G w kodzie DNA wynosi: {procent}%")
