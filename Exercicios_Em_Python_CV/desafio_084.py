#Faça um programa que leia nome
#e peso de várias pessoas,
#guardando tudo em uma lista
#No final, mostre:
#a) Quantas pessoas foram cadastradas
#b) Uma listagem com as pessoas mais pesadas
#c) Uma listagem com as pessoas mais leves

cadastro_de_pessoas = list()
lista_aux = []

maior_peso = None
menor_peso = None
while True:
	nome = str(input("Digite o nome da pessoa a ser cadastrada:"))
	peso = float(input("Digite o peso da pesssoa:"))
	
	lista_aux.append(nome)
	lista_aux.append(peso)
	cadastro_de_pessoas.append(lista_aux[:])
	lista_aux.clear()
	
	if maior_peso == None:
		maior_peso = peso
	elif maior_peso < peso:
		maior_peso = peso
	if menor_peso == None:
		menor_peso = peso
	elif menor_peso > peso:
		menor_peso = peso
	
	op = str(input("Deseja continuar[S/N]:")).strip()[0]
	if op in 'Nn':
		break
print(f"Total de pessoas cadastradas:{len(cadastro_de_pessoas)}")
print(f"Lista de pessoas mais pesadas:")
for i in cadastro_de_pessoas:
	if i[1] == maior_peso:
		print(i[0], end = " ")
print()
print(f"Lista de pessoas mais leve:")	
for i in cadastro_de_pessoas:
	if i[1] == menor_peso:
		print(i[0], end = " ")
	

