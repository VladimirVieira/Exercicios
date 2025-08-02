#Desenvolva um programa que leia o primeiro termo
#e a razão de uma PA 
#no final mostre os 10 primeiros termos dessa progressão 
primeiro_termo = int(input('Digite o primeiro termo da PA:'))
razao_da_pa = int(input('Digite um número inteiro que compreende a razao da PA:'))


for i in range(0,10):
    print(primeiro_termo, end = ' ')
    primeiro_termo += razao_da_pa