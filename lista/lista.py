# lista studentow

q = ""
lista_studentow = []

lista = open("lista.txt", "a+")
lista = open("lista.txt", "r")
print(lista.read())
lista.close()

while True:
    student = input("Nowy student: Imię Nazwisko Grupa (q aby zakończyć): ")
    if student == 'q':
        break
    lista_studentow.append(student)

lista = open("lista.txt", "a+")
lista.write("\n".join(lista_studentow))
lista.write("\n")
lista.close()
