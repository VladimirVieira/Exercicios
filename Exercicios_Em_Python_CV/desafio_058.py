#Melhore o jogo do desafio 028 onde o computador vai pensar em
#um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar
#mostrando  no final quantos palpites foram necessário para
#vencer
from random import randint

num_aleatorio = randint(0,10)

op = -1
cont = 0

while op != num_aleatorio:
    op = int(input('Digite chute [0-10]:'))
    cont+=1
    if op < num_aleatorio:
        print('O número é maior')
    elif op > num_aleatorio:
        print('O número é menor')
    else:
        print('acertou') 
print('Você precisou de {} tentativas'.format(cont))
