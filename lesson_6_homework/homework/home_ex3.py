# Improve the password generator
"""
Inbunatatiti acest generator de parole, astfel in cat sa fie posibil sa genereze parole ce contin atat litere,
 cat si cifre si caractere speciale.
"""

import string
import random

all_letters = list(string.ascii_letters)
print(all_letters)
pass_length = int(input('Pass length'))

password = ''
for a in range(pass_length):
    letter_index = random.randrange(0, len(all_letters))
    password += all_letters[letter_index]
    print(password)
