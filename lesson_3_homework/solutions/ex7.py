"""
Numărarea caracterelor
Scrieți un program care
 primește un șir de caractere ca intrare
 și numără de câte ori apare un caracter specific (introdus in consola).

 Numarul de caractere trebuie sa fie considerat indiferent daca e majuscula sau minuscula
"""
# Solution
sir = input("Sirul")
caracter = input("Caracterul")
caractert_lower = caracter.lower()
print(sir.lower().count(caractert_lower), "ori")
