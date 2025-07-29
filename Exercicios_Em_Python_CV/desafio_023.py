#Faça um programa que leia um número de 0 a 9999
#e mostre na tela cada um dos digitos separados
numero = int(input('Digite um número inteiro entre 0 e 9999'))
print('Unidade:{}'.format(numero%10))
print('Dezena:{}'.format((numero%100)//10))
print('Centena:{}'.format((numero%1000)//100))
print('Milha:{}'.format(numero//1000))
numero_string = str(numero)
print('Milhar:',numero_string[0])
print('Centena:',numero_string[1])
print('Dezena:',numero_string[2])
print('Unidade:',numero_string[3])