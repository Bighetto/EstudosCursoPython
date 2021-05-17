#xargs - Vários argumentos.

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x = soma(3,4,7,10)

print (x)

#O return é na linha abaixo um pouco atrás do comando anterior.

#Utilizado o forloop para somar um numero com o outro.

#linha 6= resultado soma com o num (3,4,7,10).
