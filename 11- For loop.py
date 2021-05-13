#Imprimir de 1 a 5.

'''Forma repetitiva.
print ('1')
print ('2')
print ('3')
print ('4')
print ('5')
'''

for numero in range (1, 6):
    print (numero)

'''Python executa como index, ou seja: numero 0,1,2,3...
Comando "range" organiza de onde começa até onde vai.
range (1(começo), 6(fim=5 total)).'''

#For loop com Letras:

palavra = 'Instagram'

for letra in palavra:
    print (f'{letra} esta dentro da palavra {palavra}')

'''Maneira simplificada ao inves de colocar letra
por letra igual o exemplo do número la em cima.
'''

compra_confirmada = True
dados_compra = 'Compra no valor de 12.50 realizada e entregue.'

'''
Enviar um email com os detalhes de compra online
(Máximo 3 tentativas) para compras confirmadas.
'''

for enviar in range(3):
  if compra_confirmada:
    print (dados_compra)
    print ('Detalhes enviados por e-mail.')
    break 
else:
    print ('Falha na compra')

''' O Break serve para parar o loop, assim que o dado for validado
ele nao executa novamente, no caso seriam 3 tentativas'''

# for loop nested

    #outer loop
     #inner loop

for numero1 in range(1,6):
    print ('Produto' + str (numero1))
    for numero2 in range(11):
        print (numero2)

''' o Outer loop que é o "numero1" vai rodar 5 vezes (1,6) do 1 ao 5;
o inner loop "numero2" vai rodar 11 vezes.
Quando o Outer loop rodar uma vez, o inner vai rodar 11 dentro,
quando completar as 11 vezes o Outer loop vai rodar mais uma vez, 
e o inner vai rodar mais 11, assim sucessivamente ate o Outer loop chegar
na 5 virada do loop, que é executado pelo comando Range.
'''

#Modificar de BIGHETTO para B I G H E T T O

palavra = 'BIGHETTO'

for spaco in palavra:
    print (f' {spaco}' , end='')

#Comando para separar palavra dentro da String.