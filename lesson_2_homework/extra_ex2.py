# Exercițiul 2: Operații numerice

# Scrie un program care preia două numere ca intrare și efectuează următoarele operații:
# - Adună cele două numere și afișează rezultatul.
# - Scade al doilea număr din primul număr și afișează rezultatul.
# - Înmulțește cele două numere și afișează rezultatul.
# - Împarte primul număr la al doilea număr și afișează rezultatul.

a = input("Atribuiti un nr. lui a: ")
b = input("Atribuiti un nr. lui b: ")
a = int(a)
b = int(b)
suma = a + b
diferenta = a - b
multiply = a * b
divizare = a / b
print(f"Suma nr. este {suma}")
print(f"Diferenta nr. este {diferenta}")
print(f"Inmultirea nr. este {multiply}")
print(f"Impartirea nr. este {divizare}")