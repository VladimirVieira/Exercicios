#Escreva um programa que leia dois números inteiros e compare-os
#mostrando na tela uma mensagem
#-o primeiro valor é maior
#-o segundo valor é maior
#-são iguais
num1 = int(input('Digite o primeiro número inteiro:'))
num2 = int(input('Digite o segundo número inteiro:'))
if num1 > num2:
    print('o {} é maior que {}'.format(num1, num2))
elif num2 > num1:
    print('o {} é maior que {}'.format(num2, num1))
else:
    print('{} e {} são iguais'.format(num1, num2))