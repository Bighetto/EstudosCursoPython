'''
Generator Expressions
    Uma forma mais rapida para listas, dicionarios, etc.
    Menos memoria alocada
    valores em bytes
'''

from sys import getsizeof

numeros = [x * 10 for x in range (1000)]
print (type (numeros))
print(getsizeof(numeros))

print ('====')

#resposta: 9016 em bytes.