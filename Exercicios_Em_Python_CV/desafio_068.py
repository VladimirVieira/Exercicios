#Faça um programa que jogue par ou impar com o computador
#O jogo só será interrompido quando o jogador perder, mostrando o total 
#de vitórias consecutivas que ele conquistou no final do jogo

from random import randint

cont = 0
while True: 
    escolha_do_pc = randint(0,5)
    escolha_do_usuario = int(input('Escolha do usuário:'))

    op = str(input('Você escolhe par ou ímpar[P/I]:'))
    
    soma = escolha_do_pc + escolha_do_usuario

    if soma%2 == 0 and op in 'Pp':
        print(f'a soma resultou em {soma} e sua escolha foi par')
    elif soma%2 != 0 and op in 'Ii':    
        print(f'a soma resultou em {soma} e sua escolha foi impar')
    else:
        break
    
    cont += 1
print('='*60)
print(f'Total de vitorias:{cont}')

    
