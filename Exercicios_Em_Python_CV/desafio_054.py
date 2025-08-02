#Crie um programa que leia o ano de 
#nascimento de sete pessoas. No final 
#mostre quantas pessoas ainda não atingiram 
#a maioridade e quantas jã são maiores 
from datetime import date 
cont_maioridade = 0
cont_menoridade = 0

for i in range(0,7):
    ano_de_nascimento = int(input('Ano de nascimento:'))
    ano_atual = date.today().year 
    ano_de_nascimento = ano_atual - ano_de_nascimento 
    
    if ano_de_nascimento >= 18:
        cont_maioridade += 1 
    else:
        cont_menoridade += 1 
        
print('Numero de pessoas com maior idade:{}'.format(cont_maioridade))
print('Numero de pessoas com menor idade:{}'.format(cont_menoridade))