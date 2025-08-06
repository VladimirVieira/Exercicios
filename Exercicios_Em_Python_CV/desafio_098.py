#Faça um programa que tenha uma função
#chamada contador(),  que receba três
#parâmetros: início, fim e passo
#Seu programa tem que realizar três
#contagens através da função criada
#a) De 1 até 10, de  1 m 1
#b) De 10 até 0, de 2 em 2
#c) Uma contagem personalizada

def contador(a, b, c):
	for i in range(1,11):
		print(i, end = " ")
	
	print(" ")
	print("#"*70)
	
	for j in range(10,0,-2):
		print(j, end = " ")
	
	print(" ")
	print("#"*70)
	
	for k in range(a, b, c):
		print(k, end = " ")
		
	print(" ")

contador(3,30,3)
