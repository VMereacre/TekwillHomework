"""
Avand lista de mai jos.

Adaugati in ea elementele **4**, **5** si **6**.

Afișați rezultatele
"""

list_1 = [1,2,3]

# Utilizind extend
list_2 = [4,5,6]
list_1.extend(list_2)
print(list_1)

# Utilizind concatenare
list_2 = [4,5,6]
list_1 += list_2
print(list_1)

# Utilizind append
list_2 = [4,5,6]
for elem in list_2:
    list_1.append(elem)
print(list_1)