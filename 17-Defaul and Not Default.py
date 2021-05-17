'''
Funções (Functions)
    DRY - Don't repeat yourself.
    Parametro ---> Argumento.
    Default = Aquele que você define o valor no parâmetro.
    Non-Default = Aquele que você não define o valor no parâmetro.
'''

#Exemplo Default:

def boas_vindas (quantidade, nome='Fernando'):
    print (f'Olá {nome}.')
    print (f'Temos {str (quantidade)} laptops em estoque.')


boas_vindas(7)

#REGRA: COLOCAR NUN-DEFAULT PRIMEIRO E NO FINAL  O DEFAULT.
