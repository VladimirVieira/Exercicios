#Crie um programa que vai ler vários
#números e colocar em uma lista
#Depois disso, mostre:
#a)Quantos números foram digitados
#b)a lista de valores, ordenada de forma decrescente
#c)Se o valor 5 foi digitado e está    ou não na lista

lista = list()

while True:

	num = int(input("Digite um número inteiro:"))
	if num not in lista:
		lista.append(num)
	

	op = str(input("Deseja continuar[S/N]:")).strip()[0]
	
	if op in "Nn":
		break
lista.sort(reverse = True)
print(f"Quando numeros foram digitados:{len(lista)}")
print(f"Lista ordenada de forma decrescente:{lista}")

if 5 in lista:
	print("O valor 5 não foi digitado")
else:
	print("O valor 5 tá na lista")

