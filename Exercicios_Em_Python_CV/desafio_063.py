#Escreva um programa que leia um número n inteiro qualquer e mostre
#na tela os n primeiros elementos de uma sequencia de Fibonacci

n = int(input('Digite a quantidade de termos da sequencia de fibonacci:'))
termo = 1
termo_anterior = 0
valor = 0
while n > valor :
    if valor == 0:
        print(termo_anterior, end = ' ')
        valor += 1
    elif valor == 1:
        print(termo, end = ' ')
        valor+=1
    else:
        aux = termo + termo_anterior
        termo_anterior = termo
        termo = aux 
        valor+=1
        print(aux, end = ' ')
print('')
    
