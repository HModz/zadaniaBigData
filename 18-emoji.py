#emoji

emoji = {":)":"\U0001F600", ":(":"\U0001F61F"}

tekst = input("Wpisz tekst: ")

def Emoji(tekst):
    slowa = tekst.split(" ")
    zmieniony = ""
    for i in slowa:
        zmieniony += emoji.get(i, i) + " "
    print(zmieniony)

Emoji(tekst)
