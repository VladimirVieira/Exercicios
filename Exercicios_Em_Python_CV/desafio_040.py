#crie um programa que leia duas notas de um aluno e calcule sua média
#mostrando uma mensagem no final, de acordo com a média atingida
#Média abaixo de 5: "Reprovado"
#Média entre 5 e 6.9: "Recuperação"
#Média 7 ou superior: "Aprovado"
nota1 = float(input('Digite a sua primeira nota:'))
nota2 = float(input('Digite a sua segunda nota:'))
media = (nota1+nota2)/2 
if media<5:
    print('Média {:.2f}: status reprovado'.format(media))
elif 5<=media<7:
    print('Média {:.2f}: status recuperação'.format(media))
elif media>=7:
    print('Media {:.2f}: status aprovado'.format(media))