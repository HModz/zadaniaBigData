#lista studentow

lista = open("lista.txt", "w+")
q = ""
lista_studentow = []

while True:
  student = input("Podaj Imię Nazwisko Grupe (q aby zakończyć): ")
  if student == 'q':
    break
  lista_studentow.append(student)

print(lista_studentow)
