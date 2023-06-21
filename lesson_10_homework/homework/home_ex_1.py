'''
1. De la consola se va introduce o bucata de text.
2. Calculati de cate ori fiecare cuvant a fost folosit.
3. Afisati informatia.
'''

text = input('Introduceti un text : ')

text_words = text.split()

word_dictionary = dict()

for word in text_words:
    word_dictionary[word] = word_dictionary.get(word, 0) + 1
print(word_dictionary)
for word in word_dictionary:
    print(f'Word "{word}" was use {word_dictionary[word]} times')
