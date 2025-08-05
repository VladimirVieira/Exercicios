#Faça um programa que leia 5 valores
#numéricos e guarde-os em uma lista
#No final, mostre qual foi o maior e o menor
#valor digitado e as suas respectivas
#posições na lista

lista_de_numeros = list()

for i in range(5):
	valor = int(input("Digite um número:"))
	lista_de_numeros.append(valor)
	
print(f"Mostre o maior valor:{max(lista_de_numeros)}")
print(f"Mostre o menor valor:{min(lista_de_numeros)}")
