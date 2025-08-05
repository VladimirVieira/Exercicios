#Crie um programa onde o usuário possa
#digitar vários valores numéricos
#e cadastre-os em uma lista
#Caso o número já exista lá dentro, ele não será adicionado
#No final, serão exibidos
#Todos os valores únicos
#digitados, em ordem crescente

lista_de_numero = []

while True:
	numero = int(input("Digite um número inteiro:"))
	if numero not in lista_de_numero:
		lista_de_numero.append(numero)
	
	op = str(input("Deseja continuar:")).strip()[0]
	
	if op in 'Nn':
		break
		
print(f"Lista ordenada:{sorted(lista_de_numero)}")
