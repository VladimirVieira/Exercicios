#Crie um programa que tenha uma função fatorial que receba dois
#parâmetros: o primeiro que indique o número a calcular e o outro
#chamado show, que será um valor lógico(opcional) indicando se
#será mostrado ou não na tela o processo de cálculo fatorial

def fatorial(a, show = False):
	"""
	-> Calcula o Fatorial de um número
	:param a: O número a ser calculado
	:param show: (opcional) mostrar ou não mostrar como foi obtido o resultado
	:return: O valor de Fatorial de um número n
	"""
	produtorio = 1
	if show == True:
		for i in range(a,1,-1):
			
			print(i, end = 'x')
			produtorio *= i
		print(f'{1} = {produtorio}')
	else:
		for i in range(a,1,-1):
			
			produtorio *= i
		print(f'Resultado {produtorio}')
		
fatorial(5)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
