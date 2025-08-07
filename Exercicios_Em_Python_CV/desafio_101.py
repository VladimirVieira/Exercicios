#Crie um programa que tenha uma função chamada voto() que vai
#receber como parâmetro o ano de nascimento de uma pessoa
#retornando um valor lieral indicando se uma pessoa tem voto
#negado, opcional ou obrigatorio

from datetime import date
def voto(ano_de_nascimento):

	idade = date.today().year - ano_de_nascimento
	status = None
	if idade < 16:
		status = 'negado'
	elif 18< idade < 66:
		status = 'obrigatorio'
	else:
		status = 'opcional'
	return f'sua idade é: {idade} logo o seu status de votação é:{status}'
	
print(voto(int(input("Informe o seu ano de nascimento:"))))
	
