#Crie um programa onde 4 jogadores joguem um dado e tenham
#resultado aleatorios. Guarde esses resultados em um dicionario
#No final, coloque esse dicionario em ordem, sabendo
#que o vencedor tirou o maior número o dado

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1,6), 'jogador2': randint(1,6),'jogador3': randint(1,6), 'jogador4' : randint(1,6)}

for i,j in jogo.items():
	print(f"{i} tirou {j}")
	sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1),reverse=True)

for i, j in enumerate(ranking):
	
	print(f'{i} lugar: {j[0]} com {j[1]}')
