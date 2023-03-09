word =  'itproger, proger , it'
#print(word.count('p'))
#print(word.find('p'))
hobby = word.split (', ')

for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()
#print(hobby)  # так велика буква кожного слова в списеку
#print(word.capitalize()) в такому випадку велика тільки буква 1 слова в списку

result = ', '.join(hobby)
print(result)

