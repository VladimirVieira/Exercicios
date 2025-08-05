#Crie um programa que vai ler váios números e colocar em uma
#lista. Depois disso, crie duas listas extras que vão conter
#apenas os valores pares e os valores ímpares digitados
#Ao final mostre o conteúdo das três listas geradas

lista_geral = []
lista_pares = []
lista_impares = []

while True:
	num = int(input('Digite um elemento para inserir na lista:'))
	lista_geral.append(num)
	if num%2 == 0:
		lista_pares.append(num)
	else:
		lista_impares.append(num)
	op = str(input("Deseja continuar:"))[0]
	if op in 'Nn':
		break
		
print(f"Lista de numeros pares:{lista_pares}")
print(f"Lista de numeros impares:{lista_impares}")
print(f"Lista de numeros geral:{lista_geral}")
