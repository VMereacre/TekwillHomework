"""
Citiţi de la tastatură un număr întreg.
Dacă numărul este negativ, afişaţi mesajul `"That number is less than 0!"`.
Dacă este pozitiv, afişaţi `"That number is greater than 0!"`.
Dacă nu este nici negativ nici pozitiv afişaţi mesajul `"You picked 0!"`.
"""
print("Introduce un nr. intreg de la tastatura")
x = int(input("x = "))
if x < 0:
    print("That number is less than 0!")
elif x > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")