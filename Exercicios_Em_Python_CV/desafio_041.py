#A confederação nacional de natação precisa de um programa que leia 
#o ano de nascimento de um atleta e mostre a sua categoria, de acordo
#com a idade
from datetime import date 

ano_de_nascimento = int(input('Digite seu ano de nascimento:'))
idade = date.today().year - ano_de_nascimento 
print('A sua idade:{}'.format(idade))
if idade<9:
    print('Mirim')
elif 8<=idade<14:
    print('Infantil')
elif 14<=idade<19:
    print('Junior')
elif 19<=idade<25:
    print('Senior')
else:
    print('Master')