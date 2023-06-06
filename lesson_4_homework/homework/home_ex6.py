"""
Scrieţi un program care citeşte de la tastatură numele unei persoane.
Dacă numele nu începe cu literă mare, atunci programul transformă valoarea citită în numele persoanei scris cu literă mare.
După aceasta, afişează la ecran `"Salut, <numele citit de la tastatura care începe cu litera mare>!"`.
"""
nume = input("Scrie numele aici : ")
prima_litera = nume[0]
if prima_litera.islower():
    nume = nume.capitalize()
    print(f"Salut, {nume}!")
else:
    print(f"Salut, {nume}!")

# Alternativa
if not prima_litera.isupper():
    nume = nume.capitalize()
    print(f"Salut, {nume}!")
else:
    print(f"Salut, {nume}!")