#Aprimore o desafio anterior, mostrando no final
#a) A soma de todos os valores pares digitados
#b) A soma dos valores da terceira colua
#c) O maior valor da segunda linha

matriz = list()
valores_pares = 0
terceira_coluna = 0
maior = None
for i in range(3):
	lista_aux = []
	for j in range(3):
		valor = int(input("Digite um número inteiro:"))
		lista_aux.append(valor)
		if valor % 2 == 0:
			valores_pares += valor
		if j == 2:
			terceira_coluna += valor
	matriz.append(lista_aux[:])
	if i == 1:
		maior = max(lista_aux)
	lista_aux.clear()
	
for i in matriz:
	for j in i:
		print(f"[{ j }]", end = " ")
	print()
	
print("="*60)
print(f"A soma de todos os valores pares digitados:{valores_pares}")
print(f"A soma dos valores da terceira coluna:{terceira_coluna}")
print(f"Maior valor:{maior}")
