#Escreva um programa que faça o computador pensar
#em um número inteiro entre 0 e 5
#e peça para o usuário tentar desconbrir
#qual foi o número escolhido pelo computador
#O programa deverá escrever na tela se o usuário perdeu ou venceu
from random import randint
escolha_do_computador = randint(0,5)
escolha_do_usuario = int(input('Digite um número entre 0-5:'))
if escolha_do_computador == escolha_do_usuario:
    print('O computador escolheu {} e você escolheu {}, logo voê acertou e venceu!'.format(escolha_do_computador, escolha_do_usuario))
else:
    print('O computador escolheu {} e você escolheu {}, logo você errou e perdeu!'.format(escolha_do_computador, escolha_do_usuario))