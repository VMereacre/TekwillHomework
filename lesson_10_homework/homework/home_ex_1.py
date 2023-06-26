'''
1. De la consola se va introduce o bucata de text.
2. Calculati de cate ori fiecare cuvant a fost folosit.
3. Afisati informatia.
'''

text = input('Introduceti un text : ')

text_words = text.split()

words_count = dict()

for word in text_words:
    words_count[word] = words_count.get(word, 0) + 1

for word in words_count:
    print(f'Cuvintul "{word}" a fost folosit de {words_count[word]} ori')
