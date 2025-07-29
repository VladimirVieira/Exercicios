#Leia um número inteiro e mostre
#na tela se ele é par ou ímpar
numero = int(input('Digite um número inteiro qualquer:'))
if numero%2 == 0:
    print('O numero {} é par'.format(numero))
else:
    print('O numero {} é ímpar'.format(numero))