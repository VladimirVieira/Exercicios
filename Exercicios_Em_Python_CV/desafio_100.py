#Faça um programa que tenha uma lista chamada números e duas
#funções chamadas sorteia() e somaPar(). A primeira funções vai
#sortear 5 números e vai colocá-los dentro da lista e a segunda
#função vai mostrar a soma entre todos os valores pares
#sorteados pela função anterior



from random import randint

def somarPar(lista):
	somatorio = 0
	
	for i in lista:
		if i%2 == 0:
			somatorio += i
	print(f"Somatorio:{somatorio}")

def sorteia():
	lista_de_numeros = []
	for i in range(5):
		num = randint(1,10)
		lista_de_numeros.append(num)
	print(f"Lista gerada:{lista_de_numeros}")	
	somarPar(lista_de_numeros)



sorteia()
