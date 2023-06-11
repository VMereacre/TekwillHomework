"""
BMI Calculator
Write a program that takes a person's weight (in kilograms) and height (in meters) as input and calculates their Body Mass Index (BMI).
Then classify the BMI into the following categories:

Underweight (BMI < 18.5)
Normal weight (BMI between 18.5 and 24.9)
Overweight (BMI between 25 and 29.9)
Obesity (BMI 30 or greater)


Calculator BMI
Scrie un program care primește greutatea unei persoane (în kilograme) și înălțimea (în metri) ca intrare și calculează Indicele de Masă Corporală (BMI).
Apoi clasifică BMI-ul în următoarele categorii:

Subponderal (BMI < 18,5)
Greutate normală (BMI între 18,5 și 24,9)
Supraponderal (BMI între 25 și 29,9)
Obezitate (BMI 30 sau mai mare)

Pentru a calcula Indicele de Masă Corporală (BMI), urmează pașii de mai jos:

1. Ia greutatea persoanei în kilograme și înălțimea în metri.
2. Calculează pătratul înălțimii (înmulțește înălțimea cu ea însăși).
3. Calculează BMI-ul utilizând formula: BMI = greutate / înălțime^2, unde greutatea este în kilograme și înălțimea este în metri.
4. Rezultatul obținut va fi indicele de masă corporală al persoanei.

"""
print('Indica masa corporala in kilograme si inaltimea in metri :')
masa = float(input('Greutatea : '))
inaltime = float(input('Inaltime : '))

imc = masa / inaltime ** 2
print(f'IMC = {imc}')

if imc < 18.5:
    print('IMC-ul indica la greutate subponderala!')
elif 18.5 >= imc <= 24.9:
    print('IMC-ul indica la greutate normala!')
elif 25 >= imc <= 29.9:
    print('IMC-ul indica la greutate supraponderala!')
else:
    print('IMC-ul indica la obezitate!')
