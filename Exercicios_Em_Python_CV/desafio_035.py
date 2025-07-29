#Desenvolva um programa que leia o comprimento de três retas
#e diga ao usuário se elas podem ou não formar um triangulo

l1 = int(input('Digite o tamanho do primeiro lado do triângulo:'))
l2 = int(input('Digite o tamanho do segundo lado do triângulo:'))
l3 = int(input('Digite o tamanho do terceiro lado do triângulo:'))

if l1>(l2+l3) or l2>(l1+l3) or l3>(l1+l2):
    print('os lados {}, {} e {} não formam um triângulo'.format(l1, l2, l3))
else:
    print('os lados {}, {} e {} formam um triângulo'.format(l1, l2, l3))
    