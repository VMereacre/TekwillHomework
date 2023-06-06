"""
Scrieţi un program care verifică dacă litera "a" se află pe a 2-a poziţie într-un String citit de la tastatură.
"""
sir_caractere = input("Scrie un sir cu minim 2 caractere : ")
if len(sir_caractere) < 2:
    print("Sirul are mai putin de 2 caractere!")
else:
    a = "a"
    A = "A"
    caracter2 = sir_caractere[1]
    if caracter2 == a or caracter2 == A:
        print("In sirul de caractere pe a 2-a pozitie se afla litera \"a\"")
    else:
        print("In sirul de caractere pe a 2-a pozitie nu-i litera \"a\"")
