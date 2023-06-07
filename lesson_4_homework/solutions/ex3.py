"""
Citiţi de la tastatură un număr întreg.
Dacă numărul este negativ, afişaţi mesajul `"That number is less than 0!"`.
Dacă este pozitiv, afişaţi `"That number is greater than 0!"`.
Dacă nu este nici negativ nici pozitiv afişaţi mesajul `"You picked 0!"`.
"""
numar = int(input("Introduceți un număr întreg: "))

# Verificarea valorii numărului și afișarea rezultatului corespunzător
if numar < 0:
    print("That number is less than 0!")
elif numar > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")

# Also correct
# if numar < 0:
#     print("That number is less than 0!")
# if numar > 0:
#     print("That number is greater than 0!")
# if numar == 0:
#     print("You picked 0!")


# if numar < 0:
#     print("That number is less than 0!")
# if numar > 0:
#     print("That number is greater than 0!")
# else:
#     print("You picked 0!")
