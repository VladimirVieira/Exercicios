#Crie um programa que vai gerar cinco números aleatórios e 
#colocar em uma tupla. Depois disso, mostre a listagem de números gerados 
#e também indique o menor e o maior valor que
#estão na tupla

from random import randint

numeros_aleatorios = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f"Listagem dos numeros gerados:{numeros_aleatorios}")
print(f"Maior valor:{max(numeros_aleatorios)}")
print(f"Menor valor:{min(numeros_aleatorios)}") 
