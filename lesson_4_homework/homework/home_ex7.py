"""
Scrieți un program pentru a citi temperatura de la utilizator și pentru a afișa un mesaj adecvat în funcție de starea temperaturii de mai jos.
Temp -40-(-10) atunci 'Vremea extrem de rece'
Temp -10-0 atunci 'Vremea foarte rece'
Temp 0-10 atunci 'Vreme rece'
Temp 10-20 atunci 'Vreme normala'
Temp 20-30 atunci 'Vreme calda'
Temp 30-40 atunci 'Este foarte cald'
Temp >=40 atunci 'Este extrem de cald'
"""
print("Indicati temperatura pentru a afisa starea vremii!")
temp = float(input("Temperatura : "))
if temp < -40:
    print('Valoare indisponibila')
elif temp >= -40 and temp < -10:
    print("Vremea extrem de rece")
elif temp >= -10 and temp < 0:
    print("Vremea foarte rece")
elif temp >= 0 and temp < 10:
    print("Vreme rece")
elif temp >= 10 and temp < 20:
    print("Vreme normala")
elif temp >= 20 and temp < 30:
    print("Vremea calda")
elif temp >= 30 and temp < 40:
    print("Este foarte cald")
else temp >= 40:
    print("Este extrem de cald")