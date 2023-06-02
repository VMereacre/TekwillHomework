# Exercițiul 3: Conversie de temperatură

# Scrie un program care preia o temperatură în grade Celsius ca intrare și o convertește în grade Fahrenheit.
# Formula de conversie este: Fahrenheit = Celsius * 9/5 + 32. Afișează temperatura convertită.

celsius = input("Indicati temperatura in grade Celsius : ")
celsius = float(celsius)
fahrenheit = celsius * 9/5 + 32
print(f"Temperatura convertita in grade Fahrenheit este : {fahrenheit}")