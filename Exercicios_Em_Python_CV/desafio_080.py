#Crie um programa onde o usuário
#possa digitar cinco valores
#numéricos e cadastre-os em uma lista
#já na posição correta de inserção
#sem usar o sort()
#No final, mostre a lista ordenada

lista = list()

for i in range(5):
	num = int(input("Digite um numero inteiro:"))
	if num not in lista:
		if i == 0:
			lista.append(num)
		else:	
			pos = 0
			for j in range(len(lista)):
				if lista[j] < num:
					pos = j
				
			lista.insert(pos, num)
				
print(f"Lista finalizada:{lista}")
					
