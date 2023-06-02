# Exercițiul 1: Atribuirea variabilelor

# Scrie un program care atribuie valori celor două variabile, `a` și `b`, și apoi schimbă valorile lor.
# Afișează valorile lui `a` și `b` înainte și după schimbare.

a = input("Atribuiti valoare lui a: ")
b = input("Atribuiti valoare lui b: ")
print("a = " + a + " ; b = " + b)
x = a
a = b
b = x
print("Dupa schimbare a = " + a + " ; b = " + b)