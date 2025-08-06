#Crie um programa onde o usuário possa digitar sete
#valores numéricos e cadastre-o em uma lista única que mantenha
#separados os valores pares e ímpares. No final, mostre os
#valores pares e ímpares em ordem crescente

lista_de_numeros = [[],[]]
for i in range(7):
	num = int(input("Digite um número inteiro:"))
	if num % 2 == 0:
		lista_de_numeros[0].append(num)
	else:
		lista_de_numeros[1].append(num)
		
print(f'valores pares:{sorted(lista_de_numeros[0])}')
print(f'valores impares:{sorted(lista_de_numeros[1])}')
