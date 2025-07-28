#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
num = int(input('Digite um número inteiro:'))
print('Vamos obter o dobro do número {}:{}'.format(num, num*2))
print('Vamos obter o triplo do número {}:{}'.format(num,num*3))
print('Vamos obter a raiz quadrada de {}:{}'.format(num,num**(1/2)))
print('Vamos obter a raiz quadrada de {}:{}'.format(num,pow(num,(1/2))))