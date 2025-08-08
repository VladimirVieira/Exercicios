#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo 
#agora a possibilidade de digitação de um número de tipo inválido
#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

def leiaInt(msg):
	while True:
		try:
			n = int(input(msg))
		except (ValueError, TypeError):
			print('\033[31m Erro: por favor, digite um numero inteiro válido.\033[m')
			continue
		except (KeyboardInterrupt):
			print('Entrada de dados interrompida pelo usuário')
			return 0
		else:
			return n
			
def leiaFloat(msg):
	while True:
		try:
			n = float(input(msg))
		except (ValueError, TypeError):
			print('\033[31m Erro: por favor, digite um numero inteiro válido.\033[m')
			continue
		except (KeyboardInterrupt):
			print('Entrada de dados interrompida pelo usuário')
			return 0
		else:
			return n

num = leiaInt('Digite um valor: ')
num2 = leiaFloat('Digite um valor real:')
print(f'O valor inteiro digitado foi {num} e o valor real foi {num2}')


