"""
Scrieți un program care cere utilizatorului să introducă o parolă.
Dacă parola conține cel puțin 8 caractere și include atât litere mari,
cât și litere mici, afișați mesajul „Parolă puternică”.
În caz contrar, afișați mesajul „Parolă slabă”.
"""
print("Introduceti o parola formata din litere!")
password = input('Parola : ')
lungime = len(password)-1
if not password.islower() and lungime >= 8:
    print('Parolă puternică')
else:
    print('Parolă slabă')