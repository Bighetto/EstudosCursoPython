'''
-Dicionário não usa o formato index (0,1,2,3,4,5...)
-Utiliza a forma de Key (configurar igual abaixo)
-Aceita sring, int, float, boolean...
'''

#realizar a configuração utilizando {}
aluno = {'nome': 'Arthur', 'idade': 20, 'nota': 9.5, 'aprovado': True}

#print (aluno['aprovado'])
#Executar o print em campo determinado pelo nome da KEY.

'''comando para atualizar um campo:

aluno ['nome'] = 'Fernando'

print (aluno)
'''
aluno.update ({'nome': 'Amilton', 'nota': 4.5,'endereço': 'Rua Fernando de Noronha 45', 'aprovado': False})

#Se adicionar qualquer valor no meio do codigo que não esteja pré-definido, o mesmo vai para o final no resultado.

print (aluno.get ('estado', 'Não Informado') )
#comando para responder caso o key e o value não esteja na lista.

del aluno ['idade']#comando para remover alguma key.

#FOR LOOP NO DICIONARIO.

for keys, values in aluno.items():#visualizar as chaves e valores dentro do Dicionario.
    print (keys, values)

for x in aluno.values():#visualizar os valores dentro do Dicionario.
    print (x)


#Maneira mais facil de visualizar e programar comandos dentro do Dicionario.

aluno2 = {
    'nome': 'Arthur', 
    'idade': 20, 
    'nota': 9.5,
    'aprovado': True,
    'materias': ['Matematica', 'Ingles', 'História', 'Geografia']
    }


for x in aluno2.values():
    print (x)