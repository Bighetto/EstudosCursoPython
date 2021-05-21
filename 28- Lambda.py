#Lambda Function
    # É uma função 
    # Pode ter vários argumentos mas somente  1 expressão
    # Bastante utilizda dentro de outras funções.
    # Codigo mais 'clean'

#def somar(x):
#    return x +10

#print (somar (2))

'''
somar10 = lambda x, y: x + y + 10
#print (somar10(2, 3))
'''

def somar(x):
    func2 = lambda x: x +10
    return func2(x) * 4

print (somar(2))
# 2 + 10 * 4 = 48