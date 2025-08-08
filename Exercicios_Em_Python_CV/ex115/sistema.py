from interface import *
from arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
	criarArquivo(arq)
	

while True:
	resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
	if resposta == 1:
		#print('Opcao 1')
		lerArquivo(arq)
	elif resposta == 2:
		#print('Opcao 2')
		#Opção de cadastrar uma nova pessoa
		cabecalho('Novo cadastro')
		nome = str(input('Digite um novo nome:'))
		idade = leiaInt('Idade:')
		cadastrar(arq, nome, idade)
	elif resposta == 3:
		cabecalho('Saindo do sistema... Até logo!')
		break
	else:
		print('\033[31mErro! digite uma opção válida!\033[m')
