#Faça um programa que tenha uma função chamada ficha(), que
#receba dois parâmetro opcionais: o nome de um jogador e 
#quantos gols ele marcou. O programa deverá ser capaz de mostrar
#a ficha do jogador, mesmo que algum dado não tenha sido
#informado corretamente

def ficha(a = 'Desconhecido', b = 0):
	print(f'O jogador {a} fez a seguinte quantidade de gols {b}')
	
ficha("", 2)
