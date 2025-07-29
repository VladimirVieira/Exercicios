#Crie um programa que leia um número real qualquer pelo teclado
#e mostre na tela a sua porção inteira
from math import trunc
valor = float(input('Digite um valor qualquer:'))
print('Porção inteira de {}:{}'.format(valor, trunc(valor)))
print('Outra forma:{}'.format(valor//1))
print('Outra forma:{}'.format(int(valor)))