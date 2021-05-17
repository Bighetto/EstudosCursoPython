#manter sequencia dos dados em uma forma variável.


cor_cliente = input ('Digite a cor desejada: ')
cores = ['roxa', 'vermelho', 'azul', 'verde']

if cor_cliente.lower() in cores:
    print ('Está dentro de cores')
else:
    print ('A cor não está disponível')

#comando .lower é para não diferenciar maiúsculas e minúsculas.
