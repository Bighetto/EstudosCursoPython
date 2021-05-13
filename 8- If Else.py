velocidade = 40

if velocidade > 100:
    print ('Acima da velocidade.')
    print ('Favor reduzir para no máximo 100.')
    print ('Dirigir nesta velocidade pode causar acidentes.')
elif velocidade < 60:
    print ('Favor acelerar para no mímimo 80 km/h')
else:
    print ('Velocidade correta.')


    '''
    O if serve como "se", o else como "se não".
        No exemplo mostrado é, se a velocidade for maior que 100, executa os comandos de
    acima da velocidade, se não for maior que 100, executa "velocidade correta".
        O elif (else if) serve para ser específico dentro do comando, não apenas se ou se não, 
    da pra programar quantas variáveis quiser utilizando elif. 
        Neste caso do exemplo de elif, foi programado para se o motorista estiver dirigindo com 
    menos de 60 km/h, é executada a mensagem para acelerar.
    '''