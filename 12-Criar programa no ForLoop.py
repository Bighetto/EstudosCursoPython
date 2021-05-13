#Criar um retangulo no Forloop

'''
@@@@@
@@@@@
@@@@@
@@@@@
'''

linhas = 4
coluna = 5
simbolo = '@'

for l in range (linhas):
    for c in range (coluna):
        print (simbolo, end='')
    print()

'''Faz o "l" rodar 4 vezes (linhas), em "c" rodando 5 vezes, com o end deixando espaço,
e o ultimo print serve pra por na proxima linha.
'''