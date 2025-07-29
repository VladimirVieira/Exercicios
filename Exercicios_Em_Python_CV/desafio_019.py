#Um professor quer sortear um dos seus quatro alunos para apagar o quadro
#Faça um programa que ajude ele, lendo o nome deles e escrevendo
#o nome do escolhido

from random import choice, randint
aluno1 = input('Primeiro nome de aluno:')
aluno2 = input('Segundo nome de aluno:')
aluno3 = input('Terceiro nome de aluno:')
aluno4 = input('Quarto nome de aluno:')
lista_de_alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = randint(0,3)
print(escolhido)
print("O nome do aluno escolhido é:{}".format(choice(lista_de_alunos)))
print("O nome do aluno escolhido é:{}".format(lista_de_alunos[escolhido]))