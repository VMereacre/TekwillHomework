"""
Scrieți un program care cere utilizatorului să introducă o propoziție.
Dacă propoziția se încheie cu un semn de întrebare ("?"),
afișați mesajul „Aceasta este o întrebare”.
În caz contrar, afișați mesajul „Aceasta nu este o întrebare”
"""
import string

propozitie = input("Introduceti o propozitie : ")
ultim = propozitie[len(propozitie) - 1]
if ultim in "?":
    print("Aceasta este o întrebare")
else:
    print("Aceasta nu este o întrebare")

#Alternativa
propozitie = input("Introduceti o propozitie : ")
if propozitie.endswith("?"):
    print("Aceasta este o întrebare")
else:
    print("Aceasta nu este o întrebare")