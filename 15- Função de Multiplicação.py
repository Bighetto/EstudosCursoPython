#Criar uma função onde precisará ser feito uma multiplicação.

def multiplicação():
    numero1 = input ('Qual o primeiro número?')
    numero2 = input ('Qual o segundo número?')
    numero1 = int (numero1)
    numero2 = int (numero2)
    resultado = (f'Seu resultado é: {numero1 * numero2}')
    print (resultado)

multiplicação()