"""
Creaţi lista `date_personale`.

Citiţi după aceasta de la tastatură **numele**, **prenumele**, **vârsta**, **înălţimea** şi **ocupaţia** utilizatorului şi adăugaţi aceste valori în lista creată.
"""
date_personale = []

nume = input('Numele : ')
prenume = input('Prenumele : ')
varsta = input('Varsta : ')
inaltime = input('Inaltimea : ')
ocupatie = input('Ocupatia : ')

date_personale.append(nume)
date_personale.append(prenume)
date_personale.append(varsta)
date_personale.append(inaltime)
date_personale.append(ocupatie)
print(date_personale)