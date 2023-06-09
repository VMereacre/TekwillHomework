"""Cititi de la utilizator, o lista de nume, separate prin virgula.

Folosind metoda `.split()` transformati textul de la utilizator intr-o lista de nume.

Pentru fiecare nume cititi nota introdusa de utilizator (numar intreg). Adaugati nota in lista `list_of_marks`.

Apoi:
* afișați pentru fiecare nume, nota care îi aparține.
* calculați suma notelor
* calculați media notelor


Completati campurile din ___ si adaugati codul necesar.

Note: Utilizati indiciele numelui pentru a afla nota dupa indice din `list_of_marks`.
"""

names = input('Dati o lista de nume separate prin virgula : ')
list_of_names = names.split(",")

list_of_marks = []

for name in list_of_names:
    mark = int(input(f'Indica nota lui {name} : '))
    list_of_marks.append(mark)
    print(f'{name} are nota {mark}')

# Codul pentru a afisa notele

marks_sum = 0
for mark in list_of_marks:
    marks_sum += mark

print(f"Suma notelor: {marks_sum}")
print(f"Media notelor: {marks_sum / mark}")