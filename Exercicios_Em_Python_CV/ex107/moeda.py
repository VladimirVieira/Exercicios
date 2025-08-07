def aumentar(valor, taxa):
	return valor + taxa

def diminuir(valor, taxa):
	return valor - taxa

def dobro(valor):
	return valor * 2

def metade(valor):
	return valor/2

def moeda(valor):
	return f'R${valor:.2f}'.replace('.',",")

def resumo(valor, taxa):
	print('='*60)
	print(f"{'Tabela de Resumo':^60}")
	print('='*60)
	print(f"Aumento : {moeda(aumentar(valor, taxa))}")
	print(f"Redução : {moeda(diminuir(valor, taxa))}")
	print(f"Dobro: {moeda(dobro(valor))}")
	print(f"Metade : {moeda(metade(valor))}")
