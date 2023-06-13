'''Exercițiul 1: Calculul factorialului
Scrieți un program care utilizează o buclă while pentru a calcula factorialul unui număr întreg pozitiv dat n.
Factorialul unui număr este produsul tuturor numerelor întregi pozitive de la 1 la n.
'''

nr_init = int(input('Indicati un nr. intreg pozitiv : '))

if nr_init < 0:
    print(f'{nr_init} este un nr. negativ!')
else:
    numar = nr_init
    factorial = 1
    while numar >= 1:
        factorial *= numar
        numar = numar -1
    print(f'Factorial de {nr_init} este {factorial}')