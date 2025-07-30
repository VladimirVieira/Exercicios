#Crie um programa que faça
#o computador jogar pedra, papel e tesoura com você
from random import randint
from time import sleep
lista_de_jogadas = ['pedra','papel','tesoura']
op_usuario = str(input('Digite sua opção [pedra, papel, tesoura]:'))
op_computador = randint(0,2)

print('opção do computador:{}'.format(lista_de_jogadas[op_computador]))
print('opção do usuario:{}'.format(op_usuario))

sleep(3)
if lista_de_jogadas[op_computador] == op_usuario:
    print('Deu empate')
elif lista_de_jogadas[op_computador] == 'pedra' and op_usuario == 'tesoura' :
    print('O computador ganhou')
elif lista_de_jogadas[op_computador] == 'tesoura' and op_usuario == 'pedra' :
    print('voce ganhou')
elif lista_de_jogadas[op_computador] == 'tesoura' and op_usuario == 'papel' :
    print('o computador ganhou')
elif lista_de_jogadas[op_computador] == 'papel' and op_usuario == 'tesoura' :
    print('você ganhou')
elif lista_de_jogadas[op_computador] == 'papel' and op_usuario == 'pedra' :
    print('o computador ganhou')
elif lista_de_jogadas[op_computador] == 'pedra' and op_usuario == 'papel' :
    print('voce ganhou')