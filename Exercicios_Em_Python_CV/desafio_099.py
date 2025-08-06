#Faça um programa que tenha uma função
#chamada maior(), que recba vários
#parâmetros com valores inteiros
#Seu programa tem que analisar todos os valores
#e dizer qual deles é o maior

def maior(*num):

	maior = None
	for i in num:
		if maior == None:
			maior = i
		elif i > maior:
			maior = i
		print(i, end = " ")
			
	print(f"Maior número:{maior}")
	
maior(3,2,5,7,4)

