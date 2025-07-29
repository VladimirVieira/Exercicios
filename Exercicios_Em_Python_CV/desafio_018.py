#Faça um programa que leia um ângulo
#qualquer e mostre na tela o valor do seno
#cosseno e tangente desse ângulo
from math import sin, cos, tan, radians
valor_do_angulo = float(input('Digite o valor do ângulo:'))
converter_angulo = radians(valor_do_angulo)
print("A par do ângulo de {} temos seno de:{}".format(converter_angulo, sin(converter_angulo)))
print("temos um cosseno de:{}".format(cos(converter_angulo)))
print("temos uma tangente de:{}".format(tan(converter_angulo)))
