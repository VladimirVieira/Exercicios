#Faça um programa que leia um 
#número inteiro e diga se ele é ou não 
#é número primo
numero_avaliado = int(input('Digite um número inteiro para verificar se é primeiro:'))
cont = 0
for i in range(1,(numero_avaliado+1)):
    if numero_avaliado % i == 0:
        cont += 1 
print('é primo' if cont == 2 else 'não é primo')
