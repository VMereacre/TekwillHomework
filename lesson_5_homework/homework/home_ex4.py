"""
Creaţi 2 liste: `elev1` şi `elev2`.

Pentru fiecare elev, cititi de la tastatură **numele**, **prenumele** şi **nota** obţinută la examen şi salvaţi datele în listele `elev1` şi `elev2`.

După aceasta, afişaţi la ecran:
* care dintre cei 2 elevi are o notă mai mare la examen (afişaţi numele şi prenumele)
* care dintre cei 2 elevi are o notă mai mică la examen (afişaţi numele şi prenumele)
* pentru fiecare elev, transformaţi numele sa fie scris cu toate literele majuscule, iar prenumele să înceapă cu literă mare. De exemplu, pentru elevul "Elon Musk", rezultatul afişat va fi "Elon MUSK"
*	afişaţi datele sub formă de tabel, folosind indexarea listelor, ca în exemplul de mai jos (Nu neaparat sa fie tabel):

| Elon | Musk | 9.5 |
|------|------|-----|
| Bill | Gates | 8.5|
"""
elev1 = []
elev2 = []
print('Introduceti datele pentru elevul 1 : ')
nume1 = input('Numele : ').upper()
elev1.append(nume1)
prenume1 = input('Prenumele : ').capitalize()
elev1.append(prenume1)
nota1 = float(input('Nota : '))


print('Introduceti datele pentru elevul 2 : ')
nume2 = input('Numele : ').upper()
elev2.append(nume2)
prenume2 = input('Prenumele : ').capitalize()
elev2.append(prenume2)
nota2 = float(input('Nota : '))


if nota1 > nota2:
    print(f'Nota mai mare are : {nume1} {prenume1}')
    print(f'Nota mai mica are : {nume2} {prenume2}')
elif nota2 > nota1:
    print(f'Nota mai mare are : {nume2} {prenume2}')
    print(f'Nota mai mica are : {nume1} {prenume1}')
else:
    print('Ambii au aceeasi nota!\n')

nota1 = str(nota1)
nota2 = str(nota2)

elev1.append(nota1)
elev2.append(nota2)

afisare_elev1 = ' |'
afisare_elev2 = ' |'

for el1 in elev1:
    afisare_elev1 += ' ' + el1 + ' |'
print(afisare_elev1)
print(' ---------------------')
for el2 in elev2:
    afisare_elev2 += ' ' + el2 + ' |'
print(afisare_elev2)