#O mesmo professor do desafio anterior quer sortear a ordem de apresentação
#de trabalho dos alunos. Faça um programa que try:
#o nome de quatro alunos e mostre a ordem sorteada

from random import shuffle
n1 = str(input('Digite o nome do primeiro aluno:'))
n2 = str(input('Digite o nome do segundo aluno:'))
n3 = str(input('Digite o nome do terceiro aluno:'))
n4 = str(input('Digite o nome do quarto aluno:'))
lista_de_alunos = [n1, n2, n3, n4]
shuffle(lista_de_alunos)
print(lista_de_alunos)