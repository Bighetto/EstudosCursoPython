idade = input ('quantos anos vc tem?')

''' Exemplo de programação completa convencional:
if idade >= 16:
    resultado = print('Voto permitido')
else:
    resultado = print ('Voto negado')

Exemplo abaixo da maneira simplificada de realizar o comando. (OPERADOR TERNARIO)
'''
idade = int (idade)

resultado = ('Voto Permitido' if idade >= 16 else 'Voto negado')

print (resultado)

#Outro exemplo diretamente encurtado abaixo:

valor=49

if 20 <= valor < 50:
    print ('Produto aceito')
else:
    print ('Produto Negado')

print (valor)

'''
Maneira de ler: Olhar diretamente pro valor no meio e verificar se ele é:
Maior ou igual a 20, (20 <= valor), e olhar se ele é menor do que 50. (valor < 50).
'''