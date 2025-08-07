#Crie um programa que tenha a função leiaInt(), que vai funcionar
#de forma semelhante a função input() do Python, só que fazendo
#a validação para aceitar apenas um valor numérico

def leiaInt(num):
	if num not in '123456789':
		return '\033[1;33;44m Digite um número válido \033[m'
	else:	
		return True

num = 0		
while True:
	num = input('Digite um número:')
	avaliacao = leiaInt(num)
	print(avaliacao)
	if avaliacao == True:
		break
	
print(f'O número digitado foi: {num}')
	
