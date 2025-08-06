#Faça um programa que ajude um jogador da mega sena a criar
#palpites. O programa vai perguntar quantos jogos serão gerados
#e vai sortear 6 número entre 1 e 60 para cada jogo, cadastrando
#tudo em uma lista composta

from random import randint

num_de_jogadas = int(input("Número de jogos:"))
lista_de_jogos = list()

for i in range(num_de_jogadas):
	jogada = []	
	while True:
		if len(jogada) == 6:
			break
		else:
			num = randint(1,60)
			if num not in jogada:
				jogada.append(num)
	lista_de_jogos.append(jogada[:])
	jogada.clear()
	
print("Lista de jogos:")
for i in lista_de_jogos:
	print(i)		 
