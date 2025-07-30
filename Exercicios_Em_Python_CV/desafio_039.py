#Faça um programa que leia o ano de nascimento de um jovem e informe
#de acordo com a sua idade, se ele ainda vai se alistar
#se é hora de se alistar
#ou se já passou o tempo de alistamento militar
from datetime import date
ano_de_nascimento = int(input('Digite o ano de nascimento:'))
idade = date.today().year - ano_de_nascimento
if idade<18:
    print('Você ainda vai se alistar!')
elif idade == 18:
    print('Tá na hora de realizar o alistamento!')
else:
    print('Passou da idade de se alistar')