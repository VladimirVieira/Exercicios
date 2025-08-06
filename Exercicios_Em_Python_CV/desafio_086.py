#Crie um programa que crie uma matriz de dimensão
#3x3 e preencha com valores lidos pelo teclado
#No final, mostre a matriz na tela, com a formatação correta

matriz = list()
for i in range(3):
	lista_aux = []
	for j in range(3):
		valor = int(input("Digite um número inteiro:"))
		lista_aux.append(valor)
	matriz.append(lista_aux[:])
	lista_aux.clear()
	
for i in matriz:
	for j in i:
		print(f"[{ j }]", end = " ")
	print()
