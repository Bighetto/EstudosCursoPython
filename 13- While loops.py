#Excelente para todos os loops dependentes de uma condição.


#Criar uma promoção de desconto de um produto que vale 750 reais.

valor = 750
dia = 0
while valor > 440:
    dia += 1
    print (f'No dia {dia} o valor do produto será {valor}')
    valor -= 20

'''
While Loop roda ate chegar no limite e terminar, 
o For loop vc determina quanto vc quer q rode com o comando "for".
'''

'''
Criar uma comissão ao funcionario que vender o produto de 10%.
Sendo vendedor de roupa, o Valor mínimo para comissão seria de R$50.
'''

valor = int (input ('Qual o valor do Produto em R$?'))

while valor > 50:
    valor = (valor * 0.10)
    print ( f'O valor que você arrecadou com a comissão da venda foi de R${valor}')
    break