#Faça um programa que leia o comprimento do cateto
#oposto  do cateto adjacente de um triangulo retângulo
#Calcule e mostre o comprimento da hipotenusa
from math import hypot
cateto_oposto = float(input('Digite o valor do cateto oposto:'))
cateto_adjacente = float(input('Digite o valor do cateto adjacente:'))
print("hipotenusa:{:.2f}".format(hypot(cateto_oposto, cateto_adjacente)))