#Faça um programa que leia as duas notas de um aluno, calcule e mostre a média
nota1 = float(input('Digite quanto você tirou na primeira nota:'))
nota2 = float(input('Digite quanto você tirou na segunda nota:'))
media = (nota1+nota2)/2 
print('A média obtida a partir das notas {} e {} é:{:.2f}'.format(nota1, nota2, media))