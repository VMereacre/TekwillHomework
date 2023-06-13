"""
Calculator BMI
Scrie un program care primește greutatea unei persoane (în kilograme) și înălțimea (în metri) ca intrare
și calculează Indicele de Masă Corporală (BMI). Apoi clasifică BMI-ul în următoarele categorii:
Subponderal (BMI < 18,5)
Greutate normală (BMI între 18,5 și 24,9)
Supraponderal (BMI între 25 și 29,9)
Obezitate (BMI 30 sau mai mare)

Pentru a calcula Indicele de Masă Corporală (BMI), urmează pașii de mai jos:
1. Ia greutatea persoanei în kilograme și înălțimea în metri.
2. Calculează pătratul înălțimii (înmulțește înălțimea cu ea însăși).
3. Calculează BMI-ul: BMI = greutate / înălțime^2, unde greutatea este în kilograme și înălțimea este în metri.
4. Rezultatul obținut va fi indicele de masă corporală al persoanei.
"""

# pas 1
greutate = float(input("Introduceti greutatea corpului in kilograme: "))
inaltime = float(input("Introduceti inaltimea in metri: "))

# pas 3
BMI = greutate / inaltime ** 2

# pas 4
if BMI < 18.5:
    print("Subponderal.")
elif BMI < 25:
    print("Greutate normala.")
elif BMI < 30:
    print("Supraponderal.")
else:
    print("Obezitate.")