#Utilizado em Listas.
#Aplicar uma função de iterable, por item. (List, tuple, dic, etc.)

lista1 = [1, 2, 3, 4, 5]

def multi(x):
    return x * 2


lista2 = map(multi, lista1)

'''
O "map" serve para multiplicar dentro da lista
pelo valor colocado. 
no caso x = 1, 2, 3, 4, 5
x(2) * 1 = 2
x * 2 = 4
x * 3 = 6
x * 4 = 8
x * 5 = 10
'''

#Converter o valor de map para list para executar o comando.

print (list(lista2))