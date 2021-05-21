'''Set (Listas)
    -Similar a listas.
    -Evita Itens duplicados.
    -Não utiliza index.
'''

list1 =([1,2,3,4,5])

s1 = {1,2,3,4,5}

#print (type (list1))
#print (type (s1))

#Diferença que o "list1" é um "list" e o "s1" é um "set"

#o comando "type" é para ver o tipo de comando que tem.

s1.add (7)

#comando de adicionar coisas no "set".
#Se adicionar o mesmo valor que já tem não aparece pois será duplicado (vantagem)

#comandos para remover:
'''
s1.remove (12) 
s1.discard (12)
O "remove" vai dar erro pois não tem no "set".
O "discard" não da erro, mesmo não tendo no "set".
'''