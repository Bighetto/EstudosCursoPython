'''
Autor: Arthur
Data: 12/05/2021
Versão 1.0
'''


#Primeira programação.
print ("ola")
print ('tudo bem?')
#Segunda Programação.
print ('que dia é hoje?')

#Variaveis:

x=2
print (x)
print (x + x)
y= 'ola'
print (y)
'''
O Z é tratado como string, ou seja = texto, seria o texto + o texto.
o V é tratado como float, ou seja = pode ser numero fracionado.
o W é tratado como numero inteiro = 1+1=2
'''
z= str (3)
v= float (4.5)
w= int (5)

print (z+z)
print (v+v)
print (w+w)

# formulando frase: O Arthur tem 18 anos e mora na cidade de Jundiai.

nome= 'Arthur'
cidade = 'Jundiai'
idade = 18

'''o Phython não executa dois tipos de dados em uma unica print, ou seja,
 apenas string ou int ou float.
 será necessário converter tudo em um único tipo para funcionar,
 no caso converter o int(idade) em String (caractere).'''

print ('O '+ nome + ' tem ' + str(idade) + ' e mora na cidade de ' + cidade + '.')

''' Problema resolvido colocando o str(idade), que a idade foi transformada em string.
Outra maneira de resolver é colocar idade=str(idade)'''

