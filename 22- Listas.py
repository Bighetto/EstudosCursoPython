#Criar lista relacionadas.

camisa0 = 'Lacoste'
camisa1 = 'Nike'
camisa2 = 'Quiksilver'

camisa = ['Lacoste', 'Nike', 'Quiksilver']
#           0           1         2

#Função para adicionar algum item no final da lista.
camisa.append ('Adidas')

#Comando para remover algo da lista.
camisa.remove ('Nike')

camisa.insert (1, 'Tommy Hilfiger')
#comando para inserir, colocando a posição do item.

camisa.pop (0)
#comando para remover a posição do item.

camisa.sort()
#comando para organizar em ordem alfabética.

print (camisa)