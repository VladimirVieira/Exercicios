#Refaça o desafio 051, lendo o primeiro
#termo e a razao de um PA, mostrando
#os 10 primeiros termos da PA usando while

primeiro_termo = int(input('Digite o primeiro termo da PA:'))
razao_da_pa = int(input('Digite a razao da PA:'))

cont = 0

while cont < 10:
    print(primeiro_termo, end = ' ')
    primeiro_termo += razao_da_pa
    cont += 1 
